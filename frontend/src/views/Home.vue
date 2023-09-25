<template>
    <div class="container mx-auto max-w-4xl h-screen mt-12">
        <!-- 0: admin, 1: user, 2: manager -->
        <div class="h-auto pt-4">
            <!-- <RoleListing :role=roleObject />
            <RoleListing :role=roleObject />
            <RoleListing :role=roleObject /> -->
            <!-- Here should use v-for to iterate through roleListings -->
            <RoleListing v-for="roleItem in roleListings" :key="roleItem.id" :role="roleItem"/>
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
        // Fetch Data 
        // I'm presuming that we are using the axios that is taught to fetch the data from the database.
        // Trying out with static data here first;
        this.roleListings = [
            {
                id: 1,
                roleName: "Software Engineer",
                roleDesc: "We are seeking a talented and motivated Software Engineer to join our dynamic team. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions. You'll collaborate with cross-functional teams to translate business requirements into scalable and efficient software systems. The ideal candidate is passionate about technology, possesses strong problem-solving skills, and has a proven track record of delivering high-quality code. Join us in shaping the future of our products and contributing to our mission of delivering innovative software solutions to our customers.",
                roleDeadline: "27/04/2023",
                skillsRequired: ["Scrum", "Python", "Design Thinking"],
            },

            {
                id: 1,
                roleName: "Software Engineer",
                roleDesc: "We are seeking a talented and motivated Software Engineer to join our dynamic team. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions. You'll collaborate with cross-functional teams to translate business requirements into scalable and efficient software systems. The ideal candidate is passionate about technology, possesses strong problem-solving skills, and has a proven track record of delivering high-quality code. Join us in shaping the future of our products and contributing to our mission of delivering innovative software solutions to our customers.",
                roleDeadline: "27/04/2023",
                skillsRequired: ["Scrum", "Python", "Design Thinking"],
            },

            {
                id: 1,
                roleName: "Software Engineer",
                roleDesc: "We are seeking a talented and motivated Software Engineer to join our dynamic team. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions. You'll collaborate with cross-functional teams to translate business requirements into scalable and efficient software systems. The ideal candidate is passionate about technology, possesses strong problem-solving skills, and has a proven track record of delivering high-quality code. Join us in shaping the future of our products and contributing to our mission of delivering innovative software solutions to our customers.",
                roleDeadline: "27/04/2023",
                skillsRequired: ["Scrum", "Python", "Design Thinking"],
            },
        ];

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
                this.roleListings = data.Listings;
                console.log(this.roleListings);
            } catch (error) {
                console.error(
                    "There was a problem with the fetch operation:",
                    error
                );
            }
        }
    }
}
</script>