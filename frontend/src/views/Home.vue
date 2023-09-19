<template>
    <div class=" container mx-auto max-w-4xl h-screen w-full flex row justify-center items-center">
        <!-- 0: admin, 1: user, 2: manager -->
        <div v-if="user.accessRights == 0" class="grid grid-cols-2 gap-8">
            <Module name="Admin module" description="" path="/listings" />
            <Module name="Admin module" description="" path="/listings" />
            <Module name="Admin module" description="" path="/listings" />
        </div>
        <div v-if="user.accessRights == 1" class="grid grid-cols-2 gap-8">
            <Module name="Admin module" description="" path="/listings" />
        </div>
        <div v-if="user.accessRights == 2" class="grid grid-cols-2 gap-8">
            <Module name="Admin module" description="" path="/listings" />
        </div>


    </div>
</template>
<script>
import Module from "../components/Module.vue"
export default {
    components: { Module },
    data() {
        return {
            user: this.$store.state.user,
            // id, fname lname, dept, email, accessRights
        };
    },
    created() {

    },
    mounted() {
        console.log(this.user);
    },
    methods: {
    }
}
</script>