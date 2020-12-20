<template>
  <div class="flex flex-col h-full">
    <div class="flex border-b-2 justify-center">
      <div class="flex-grow"></div>
      <div class="flex">
        <div class="px-6 py-2 border-b-4 border-appselectedsection">
          База закупок
        </div>
        <div class="px-6 py-2">Торги</div>
        <div class="px-6 py-2">Планы закупок</div>
        <div class="px-6 py-2">Контракты</div>
      </div>
      <div class="flex-grow"></div>
      <div class="flex items-center ml-auto">
        <div class="text-appgreytext mr-2">Закупки за</div>
        <img
          :src="require('@/assets/icons/calendar.svg')"
          class="mr-2"
          alt=""
        />
        <div>последние 30 дней</div>
      </div>
    </div>
    <div class="flex my-8 space-x-8 overflow-x-auto w-full justify-center">
      <div class="bg-white rounded flex p-8 space-x-8">
        <div class="flex flex-col">
          <div class="text-appfiltertext">Дата размещения</div>
          <input
            type="date"
            name=""
            id=""
            class="border px-2 text-appgreytext h-16"
          />
        </div>
        <div class="flex flex-col">
          <div class="text-appfiltertext">Дата обновления</div>
          <input
            type="date"
            name=""
            id=""
            class="border px-2 text-appgreytext h-16"
          />
        </div>
        <div class="flex flex-col">
          <div class="text-appfiltertext whitespace-nowrap">
            Окончание подачи заявок
          </div>
          <input
            type="date"
            name=""
            id=""
            class="border px-2 text-appgreytext h-16"
          />
        </div>
      </div>
      <div class="bg-white rounded flex p-8 space-x-9">
        <div class="flex flex-col">
          <div class="text-appfiltertext">Этап закупки</div>
          <select class="border w-32 text-appgreytext h-16">
            <option disabled selected>Все этапы</option>
          </select>
        </div>
      </div>
      <div class="bg-white rounded flex p-8 space-x-9">
        <div class="flex flex-col">
          <div class="text-appfiltertext">Цена минимальная</div>
          <input
            type="number"
            name=""
            id=""
            class="border px-2 text-appgreytext h-16"
          />
        </div>
        <div class="flex flex-col">
          <div class="text-appfiltertext">Цена максимальная</div>
          <input
            type="number"
            name=""
            id=""
            class="border px-2 text-appgreytext h-16"
          />
        </div>
      </div>
    </div>
    <div class="overflow-y-auto h-full">
      <table class="">
        <tr class="text-appthead border">
          <th
            class="border border-collapse"
            v-for="header in exportCols"
            :key="header.label"
          >
            {{ header.label }}
          </th>
        </tr>
        <tr v-for="row in items" :key="row.purchaseLink">
          <td
            class="border border-collapse p-3"
            v-for="header in exportCols"
            :key="header.label"
          >
            {{ row.common[header.field] }}
          </td>
        </tr>
      </table>
    </div>
    <div class="absolute right-0 bottom-0 p-5">
      <vue-excel-xlsx
        :data="dataOnly"
        :columns="exportCols"
        :filename="'Закупки'"
        :sheetname="'Список закупок'"
      >
        <img
          :src="require('@/assets/icons/export.svg')"
          alt=""
          class="cursor-pointer"
        />
      </vue-excel-xlsx>
    </div>
  </div>
</template>

<script>
import API from "../api/orders";
export default {
  computed: {
    items() {
      return API.get();
    },
    dataOnly() {
      return this.items.map((item) => item.common);
    },
    exportCols() {
      return [
        {
          label: "ФЗ",
          field: "",
          dataFormat: () => "44/223/615 ПП",
        },
        {
          label: "Заказчик",
          field: "org",
        },
        {
          label: "ИНН заказчика",
          field: "",
          dataFormat: () => "",
        },
        {
          label: "Регион регистрации заказчика или основной деятельсности",
          field: "Место нахождения",
        },
        {
          label: "Регион торгов",
          field: "Место доставки товара, выполнения работы или оказания услуги",
        },
        {
          label: "Сфера деятельности заказчика",
          field: "",
          dataFormat: () => "",
        },
        {
          label: "Объем торгов в руб.",
          field: "Начальная (максимальная) цена контракта",
        },
        {
          label: "Количество",
          field: "",
          dataFormat: () => "",
        },
      ];
    },
  },
  methods: {
    exportData() {},
  },
};
</script>

<style>
</style>