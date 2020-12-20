<template>
  <div id="app" class="w-full h-screen overflow-y-auto text-apptext">
    <div class="flex shadow-card h-16 items-center">
      <div class="m-4">
        <img :src="require('@/assets/logo.svg')" alt="" />
      </div>
      <div id="nav" class="w-full flex flex-grow justify-center space-x-4">
        <router-link to="/">Главная</router-link>
        <router-link to="/">Реестр</router-link>
        <router-link to="/">Закупки</router-link>
        <router-link to="/">Заявки</router-link>
        <router-link to="/">Гарантии</router-link>
      </div>
    </div>

    <div class="bg-appbg h-full w-full">
      <div class="p-16 h-full">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: "Circe";
}
</style>
