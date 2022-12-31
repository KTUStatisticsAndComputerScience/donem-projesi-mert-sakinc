<script setup lang="ts"></script>

<template>
  <div class="header">
    <div class="col-1 col-s-3"></div>
    <div class="col-10 col-s-6">
      <div class="left">
        <router-link to="/">Kargoyu Getir </router-link>
      </div>
      <div class="right">
        <router-link to="/">Kargolar</router-link>
        <router-link to="/kargo-ekle"> Kargo Ekle</router-link>
        <router-link to="/kisiler"> Personeller</router-link>
        <router-link to="/kisi-ekle"> Personel Ekle</router-link>
      </div>
    </div>
    <div class="col-1 col-s-3"></div>
  </div>
  <router-view></router-view>
</template>

<style scoped>
/* br */
br.space {
  margin-top: 3px;
  margin-bottom: 3px;
  color: inherit;
}
/* --br */
</style>
