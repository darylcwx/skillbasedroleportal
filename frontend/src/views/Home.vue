<template>
    <div class="container mx-auto max-w-4xl h-screen mt-12">
        <!-- 0: admin, 1: user, 2: manager -->
        <div class="h-auto pt-4">
            <RoleListing :role=roleObject />
            <RoleListing :role=roleObject />
            <RoleListing :role=roleObject />
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
            roleObject: { roleName: "role name here", roleDesc: "lorem ipsum description of role listing here", roleDeadline: "27/04" }
            // id, fname lname, dept, email, accessRights
        };
    },
    created() {

    },
    mounted() {
        // get/RoleListings
        // this.roleListings = response.data.roleListings

        console.log(this.user);
    },
    methods: {
    }
}
</script>