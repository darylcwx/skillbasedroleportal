<template>
  <div class="container mx-auto max-w-2xl min-h-[calc(100vh-56px)] mt-14">
    <div class="mt-4">
      <SearchFilter></SearchFilter>
    </div>
    <div class="">
      <RoleListingPanel
        v-for="roleItem in roleListings"
        :key="roleItem.id"
        :role="roleItem"
      />
    </div>
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
      // listing_id, Role_Name, Description, Deadline
    };
  },
  created() {
    // Remove static data from previous version;
  },
  mounted() {
    // get/RoleListings
    // this.roleListings = response.data.roleListings

    // console.log(this.user);
    this.fetchRoleListings();
  },
  methods: {
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
  },
};
</script>
