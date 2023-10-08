<template>
  <div class="container mx-auto max-w-2xl min-h-[calc(100vh-56px)] mt-14">
    <div class="pt-4">
      <SearchFilter @changed="getSearchValue"></SearchFilter>
    </div>
    <div v-if="this.roleListingsNotLoaded" class="placeholder-wave mt-8">
      <div
        class="placeholder bg-placeholder text-placeholder rounded-xl h-44 w-full select-none"
      >
        placeholder
      </div>
      <div
        class="mt-8 placeholder bg-placeholder text-placeholder rounded-xl h-44 w-full select-none"
      >
        placeholder
      </div>
      <div
        class="mt-8 placeholder bg-placeholder text-placeholder rounded-xl h-44 w-full select-none"
      >
        placeholder
      </div>
    </div>
    <div class="">
      <div
        v-if="!this.roleListingsNotLoaded && filteredList.length == 0"
        class="h-[calc(100vh-126px)] grid place-content-center text-white text-center"
      >
        <div class="flex flex-col">
          <ExclamationCircleIcon class="h-20 w-20 text-info mx-auto" />
          <div>
            Oops! No listings found.<br />
            Please try other search parameters.
          </div>
        </div>
      </div>
      <RoleListingPanel
        v-for="roleItem in filteredList"
        :key="componentKey"
        :role="roleItem"
      />
    </div>
    <div
      v-if="roleListingsIsEmpty"
      class="h-[calc(100vh-126px)] grid place-content-center text-white text-center"
    >
      <div class="flex flex-col">
        <ExclamationCircleIcon class="h-20 w-20 text-info mx-auto" />
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
import { ExclamationCircleIcon } from '@heroicons/vue/24/outline';

export default {
  components: { RoleListingPanel, ExclamationCircleIcon, SearchFilter },
  data() {
    return {
      user: this.$store.state.user,
      roleListings: [],
      roleListingsNotLoaded: true,
      roleListingsIsEmpty: false,
      search: '',
      componentKey: 0,
      filterSkills: [],
      currentRole: '',
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
      function findSkill(roleSkills, filterSkills) {
        if (filterSkills.length == 0) {
          return true;
        }
        for (let filterSkill of filterSkills) {
          if (roleSkills.includes(filterSkill)) {
            return true;
          }
        }
      }

      return this.roleListings.filter((roleItem) => {
        return (
          roleItem.Role_Name.toLowerCase().includes(
            this.search.toLowerCase()
          ) &&
          // && roleItem['skills'].includes(this.filterSkills) ;
          findSkill(roleItem['skills'], this.filterSkills)
        );
      });
    },
  },

  methods: {
    forceRender() {
      this.componentKey += 1;
    },

    async fetchRoleSkills() {
      try {
        this.roleListings.forEach(async (role) => {
          this.currentRole = role['Role_Name'];
          console.log(role);
          const apiUrl =
            'http://localhost:5000/api/roleskills?rolename=' + this.currentRole;
          const response = await fetch(apiUrl, { mode: 'cors' });
          const data = await response.json();
          console.log(data);
          role['skills'] = data['Role Skills'];
        });
      } catch (error) {
        console.error(error);
      }
      console.log(this.roleListings);
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
        this.fetchRoleSkills();
        this.roleListingsNotLoaded = false;
      } catch (error) {
        this.roleListingsIsEmpty = true;
        console.error(error);
      }
    },
    getSearchValue(searchValue, selectedSkillsValue) {
      this.search = searchValue.trim();
      this.filterSkills = selectedSkillsValue;
      console.log(this.filterSkills);
      console.log(this.filteredList);
      console.log('search in data is ' + this.search);
      console.log('search value is ' + searchValue);
      this.forceRender();
    },
  },
};
</script>
