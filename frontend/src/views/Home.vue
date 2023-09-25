<template>
    <div class="container mx-auto max-w-4xl h-screen mt-12">
        <!-- 0: admin, 1: user, 2: manager -->
        <div class="h-auto pt-4">
            <!-- Here should use v-for to iterate through roleListings -->
            <!-- <RoleListing v-for"roleItem in roleListings" :key"roleItem.id" :role="roleItem"/> -->
            <div v-for="roleItem in roleListings" :key="roleItem.id">
                <!-- Displayed component when not expanded. -->
                <h2>{{ roleItem.Role_Name }}</h2>
                <p>{{ roleItem.Deadline }}</p>
                <!-- Toogle Button Condition -->
                <button @click="toggleDetails(roleItem)"> Toggle Button</button>
                <!-- Displayed component when expanded -->
                <div v-if="roleItem.expanded">
                    <h2>{{roleItem.Role_Name}}</h2>
                    <p>{{ roleItem.Deadline }}</p>
                    <!--Description-->
                    <!--Skills Sets Required-->
                </div>
            </div>
            <!-- <RoleListing v-for="roleItem in roleListings" :key="roleItem.id" :role="roleItem"/> -->
        </div>
    </div>
</template>


<script>
import RoleListing from "../components/RoleListing.vue"
export default {
    components: { RoleListing },
    data() {
        return {
            user: this.$store.state.user,
            roleListings: [],
            roleObject: { roleName: "role name here", roleDesc: "lorem ipsum description of role listing here", roleDeadline: "27/04" },
            expanded: false,
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
                data.Listings.forEach((roleItem) => {
                    roleItem.Deadline = new Date(roleItem.Deadline).toDateString();
                    roleItem.expanded = false;
                });

                this.roleListings = data.Listings;
                console.log(this.roleListings);
            } catch (error) {
                console.error(
                    "There was a problem with the fetch operation:",
                    error
                );
            }
        },

        toggleDetails(roleItem) {
            roleItem.expanded = !roleItem.expanded;
        },
    },
};
</script>