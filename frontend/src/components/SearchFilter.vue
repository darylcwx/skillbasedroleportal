<template>
  <div class="d-flex flex-row align-items-stretch mt-4">
    <div class="flex-grow-1 mr-3">
      <div class="input-group rounded">
        <input
          @input="emitSearchtoParent()"
          v-model="search"
          class="form-control rounded"
          placeholder="IT, human resources, finance"
          aria-label="Search"
          aria-describedby="search-addon"
        />
      </div>
    </div>

    <div class="dropdown">
      <button
        class="btn btn-primary dropdown-toggle"
        type="button"
        id="multiSelectDropdown"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <!-- {{ dropdownButtonText }} -->
        Filter
      </button>
      <ul class="dropdown-menu" aria-labelledby="multiSelectDropdown">
        <li v-for="(item, index) in items" :key="index">
          <label class="ml-2">
            <!-- <input type="checkbox" :value="item.value" v-model="item.selected" @change="handleCheckboxChange" /> -->
            <input
              type="checkbox"
              :value="item"
              v-model="selectedItems"
              @change="emitSearchtoParent()"
            />
            {{ item }}
          </label>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['search'],
  emits: ['changed'],
  data() {
    return {
      user: this.$store.state.user,
      showDevPanel: false,
      selectedItems: [],
      items: [],
      search: '',
    };
  },
  computed: {
    dropdownButtonText() {
      const selectedItems = this.items
        .filter((item) => item.selected)
        .map((item) => item.label);
      return selectedItems.length > 0
        ? selectedItems.join(', ')
        : 'Select Items';
    },
  },
  methods: {
    emitSearchtoParent() {
      this.$emit('changed', this.search, this.selectedItems);
      console.log(this.search);
    },
    async getStaffSkillsbyID() {
      try {
        const apiUrl =
          'http://localhost:5000/api/staffskills?sid=' + this.user.id;
        const response = await fetch(apiUrl, { mode: 'cors' });
        const data = await response.json();
        console.log(data['Staff Skills']);
        this.items = data['Staff Skills'];
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
    },
    deletelater() {
      console.log(this.selectedItems);
    },
  },
  mounted() {
    const dropdownButton = document.getElementById('multiSelectDropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    dropdownMenu.addEventListener('change', this.handleCheckboxChange);
    this.getStaffSkillsbyID();
  },
};
</script>
