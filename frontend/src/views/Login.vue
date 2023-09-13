<template>
    <div class="container mx-auto max-w-lg h-screen flex row justify-center items-center">
        <div class="bg-slate-500 px-8 py-12 rounded-xl">
            <div class="">
                <hr>
                <div class="py-1">
                    <code class="text-inherit">To implement Azure SSO in future</code>
                </div>
                <hr>
            </div>
            <div class="py-3">
                <div class="flex row justify-center py-3 text-xl">Temporary Login Mock-Up</div>
                <select id="roles" v-model="role" class="w-full p-2 rounded-md">
                    <option selected>Choose a role</option>
                    <option v-for="role in roles" :value=role>{{ role }}</option>
                </select>
            </div>
            <button class="btn bg-main w-full" v-on:click="handleLogin">Login</button>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            role: "Choose a role",
            roles: []
        };
    },
    created() {
    },
    mounted() {
        this.fetchRoles()
    },
    methods: {
        async fetchRoles() {
            try {
                // Make GET request to your Flask API's /api/users route
                const apiUrl = 'http://localhost:5000/api/roles';
                const response = await fetch(apiUrl);
                const roles = await response.json();
                for (const role of roles) {
                    this.roles.push(role[1])
                }
                console.log(this.roles)
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        },
        handleLogin() {
            if (this.role === "Choose a role") {
                return
            }
            this.$router.push({ name: 'Home', params: { role: this.role } });
        },

    },
};
</script>