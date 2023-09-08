<template>
    <div className="text-pink-500">Hello we are SPM G2T2 AIS KACHANG</div>
    <div v-for="user in this.users">{{ user[1] }}</div>
</template>
<script>
export default {
    data() {
        return {
            users: [],
        };
    },
    created() {
        this.fetchUserData();
    },
    methods: {
        async fetchUserData() {
            try {
                // Make GET request to your Flask API's /api/users route
                const apiUrl = 'http://localhost:5000/api/users'
                const response = await fetch(apiUrl);
                this.users = await response.json();
                console.log(this.users)
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        },
    },
};
</script>