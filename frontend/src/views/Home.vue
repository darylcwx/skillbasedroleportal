<template>
    <div class="container mx-auto h-screen max-w-3xl">
        <!-- 0: admin, 1: user, 2: manager -->
        <div class="h-auto pt-4">
            <!-- Here should use v-for to iterate through roleListings -->
            <RoleListingPanel v-for="roleItem in roleListings" :key="roleItem.id" :role="roleItem" />
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
            // id, fname lname, dept, email, accessRights
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
                    await this.fetchDescription(roleItem);
                });

                this.roleListings = data.Listings;
                console.log(this.roleListings);
            } catch (error) {
                console.error("There was a problem with the fetch operation:", error);
            }
        },

        async fetchDescription(roleItem) {
            try {
                const apiUrl = "http://localhost:5000/api/roledesc?role_name=" + roleItem.Role_Name;
                const response = await fetch(apiUrl, { mode: "cors" });
                const data = await response.json();

                // Update the description property of the roleItem
                roleItem.description = data.description;

                console.log("Description for " + roleItem.Role_Name + ": " + data.description);
            } catch (error) {
                console.error("There was a problem with the fetch operation:", error);
            }
        },
    },
};
</script>