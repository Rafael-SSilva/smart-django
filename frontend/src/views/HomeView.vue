<template>
  <div class="content">
    <Header :name='username' />
    <main>
      <div class="table-wrapper">
        <div class="log-table">
          <h2>Log table</h2>
          <table>
            <thead>
              <tr>
                <td>S/N</td>
                <td>Location</td>
                <td>Energy (kWh)</td>
                <td>Date</td>
                <td>Cost (€/kWh)</td>
              </tr>
            </thead>
            <tbody v-if="chargeSessions?.length">
              <tr v-for="session in chargeSessions" >
                <td>{{session.id}}</td>
                <td>{{session.location}}</td>
                <td>{{session.energy_kwh}}</td>
                <td>{{getFormatedDate(session.charge_datetime)}}</td>
                <td>{{session.cost}}</td>
              </tr>
            </tbody>
          </table>
          <div class="table-pagination">
            <div class="result">
              <span>From {{ fromReg }} to {{ toReg }} of {{ total }} results</span>
            </div>
            <div class="navigation">
              <span @click="handleClickPrevious">Previous</span>
              <span @click="handleClickNext">Next</span>
            </div>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>


<script setup lang="ts">
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

import { ref } from 'vue';
import { getChargeSessions } from '../services/charge-session-service'
import { useAuthStore } from '../stores/auth-store'
import { onMounted } from 'vue';


interface ChargeSession {
  id: string
  location: string
  energy_kwh: number
  charge_datetime: string
  cost: number
}

interface ChargeSessionResult {
  count: number 
  page: number 
  page_size: number 
  next: number 
  previous: number 
  data?: ChargeSession[]
  
}

const authContext = useAuthStore()

const username = ref<string>('Profile')
const currentPage = ref<number>(1)
const pageSize = ref<number>(15)
const total = ref<number>(0)
const fromReg = ref<number>(0)
const toReg = ref<number>(0)
const chargeSessions = ref<ChargeSession[] >([])

const handleClickPrevious = async () => {
  const previousPage = currentPage.value - 1

  if((previousPage) >= 1) {
    const { data } =  await getChargeSessions(String(previousPage))
    setTableDescription((data as ChargeSessionResult))
  }
}

const handleClickNext = async () => {
  const nextPage = currentPage.value + 1

  if(toReg.value < total.value) {
    const { data } =  await getChargeSessions(String(nextPage))
    setTableDescription((data as ChargeSessionResult))
  }
}

const getFormatedDate = (dateStr = '', sep = "-") => {
  const newDate = new Date(dateStr);
  const month = newDate.getMonth() + 1
  const day = newDate.getDate()
  const year = newDate.getFullYear();
  const hours = newDate.getHours().toString()
  const minutes = newDate.getMinutes().toString()
  const seconds = newDate.getSeconds().toString()
  
  const dayString = day < 10 ? '0' + day.toString() : day.toString()
  const MonthString = month < 10 ? '0' + month.toString() : month.toString()
  const YearString = year.toString()
  
  const dateArray = [dayString, MonthString, YearString]
  const TimeArray = [hours, minutes, seconds]

  const finalDate = dateArray.join(sep);
  const finalTime = TimeArray.join(':');

  return `${finalDate} ${finalTime}`
}

const setTableDescription = ( result : ChargeSessionResult ) => {
    currentPage.value = result?.page || 0
    total.value = result?.count || 0
    chargeSessions.value = result.data || []
    pageSize.value = result.page_size || 0

    toReg.value = currentPage?.value * pageSize?.value
    fromReg.value = (toReg?.value - pageSize?.value) + 1
}

onMounted(async () => {
  if(authContext)
    username.value = authContext?.username  || username.value

    //get all sessions data
    const { data } =  await getChargeSessions()

    setTableDescription((data as ChargeSessionResult))

  }) 


</script>

<style>
  div.content {
    display: flex;
    height: 100vh;
    flex-direction: column;
    gap: 2rem;

  }
  main {
    flex: 1;

  }

  /* table styling */

  .log-table {
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    max-width: 80%;
    border-radius: 1rem;
    -webkit-box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
    box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
  }
  .log-table table {
    padding: 1rem;
    border-collapse: collapse;
    font-weight: 400;
  }

  .log-table h2 {
    padding: 1rem 1.5rem;
  }

  .log-table table thead {
    background: var(--table-header-text-color);
    font-weight: 500;
  }

  .log-table table tbody tr:nth-child(2n + 1) {
    background: var(--table-row-alternete-fill);
    background-color: var(--table-row-alternete-fill);
  }
  .log-table table td {
    padding: 0 1rem;
    line-height: 2.5rem;
    text-align: center;
  }

  .table-pagination {
    display: flex;
    padding: 1rem 2rem;
    justify-content: space-between;
    /* color: var(--table-header-text-color); */
  }

  .table-pagination .navigation {
    display: flex;
    gap: 1rem;
  }

  .table-pagination .navigation span:hover {
    cursor: pointer;
    color: var(--table-header-text-color); 
  }

</style>
