<template>
    <div class="container mx-auto h-screen max-w-2xl">
        <!-- 0: admin, 1: user, 2: manager -->
        <div class="h-auto pt-4">
            <!-- Here should use v-for to iterate through roleListings -->
            <RoleListingPanel v-for="roleItem in roleListings" :key="roleItem.id" :role="roleItem"/>
            <!-- v-if to display error text <p> if roleListings is empty -->
            <p v-if="roleListingsIsEmpty" class="text-center text-white">There are currently no listings available.</p>
        </div>
    </div>
</template>

<script>
import RoleListingPanel from "../components/RoleListingPanel.vue";

export default {
    components: { RoleListingPanel },
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
                const apiUrl = "http://localhost:5000/api/rolelistings";
                const response = await fetch(apiUrl, { mode: "cors" });
                const data = await response.json();

                // Format the date in each role item
                data.Listings.forEach(async (roleItem) => {
                    const options = { year: 'numeric', month: 'long', day: 'numeric' };
                    roleItem.Deadline = new Date(roleItem.Deadline).toLocaleString("en-US", options);
                    // Make an additional API call to fetch the description based on roleName
                });

                this.roleListings = data.Listings;
                console.log(this.roleListings);

            } catch (error) {
                console.error("There was a problem with the fetch operation:", error);
                this.roleListingsIsEmpty = true;
            }
        },

        // async fetchDescription(roleName) {
        //     try {
        //         const apiUrl = `http://localhost:5000/api/roledesc?role_name=${encodeURIComponent(roleName)}`;
        //         const response = await fetch(apiUrl, { mode: "cors" });
        //         const data = await response.json();

        //         return data.Description

        //     } catch (error) {
        //         console.error("There was a problem with the fetch operation:", error);
        //     }
        // },
    },
};
</script>