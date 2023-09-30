<template>
  <div class="container mx-auto max-w-2xl min-h-[calc(100vh-56px)] mt-14">
    <div class="pt-4">
      <SearchFilter @changed="getSearchValue"></SearchFilter>
    </div>
    <div class="">
      <RoleListingPanel
        v-for="roleItem in filteredList"
        :key="componentKey"
        :role="roleItem"
      />
    </div>
    <!-- :key="roleItem.id" -->
    <div
      v-if="roleListingsIsEmpty"
      class="h-[calc(100vh-56px)] grid place-content-center text-white"
    >
      <div class="flex flex-col">
        <ExclamationTriangleIcon class="h-12 w-12 text-red-500 mx-auto" />
        <div>
          Oops! There are currently no listings available. <br />
          Please check with HR or try again later.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RoleListingPanel from '../components/RoleListingPanel.vue';
import SearchFilter from '../components/SearchFilter.vue';
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline';

export default {
  components: { RoleListingPanel, ExclamationTriangleIcon, SearchFilter },
  data() {
    return {
      user: this.$store.state.user,
      roleListings: [],
      roleListingsIsEmpty: false,
      search: '',
      componentKey: 0,
      // listing_id, Role_Name, Description, Deadline
    };
  },
  created() {
    // Remove static data from previous version;
  },
  mounted() {
    this.fetchRoleListings();
  },

  computed: {
    filteredList() {
      return this.roleListings.filter((roleItem) => {
        return roleItem.Role_Name.toLowerCase().includes(
          this.search.toLowerCase()
        );
      });
    },
  },
  methods: {
    forceRender() {
      this.componentKey += 1;
    },

    async fetchRoleListings() {
      try {
        const apiUrl = 'http://localhost:5000/api/rolelistings';
        const response = await fetch(apiUrl, { mode: 'cors' });
        const data = await response.json();
        // Format the date in each role item
        data.Listings.forEach((roleItem) => {
          const options = { year: 'numeric', month: 'long', day: 'numeric' };
          roleItem.Deadline = new Date(roleItem.Deadline).toLocaleString(
            'en-US',
            options
          );
        });
        this.roleListings = data.Listings;
      } catch (error) {
        this.roleListingsIsEmpty = true;
        console.error(error);
      }
    },
    getSearchValue(searchValue) {
      this.search = searchValue;
      console.log(this.filteredList);
      console.log('serach in data is ' + this.search);
      console.log('search value is ' + searchValue);
      this.forceRender();
    },
  },
};
</script>
