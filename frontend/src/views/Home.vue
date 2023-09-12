<template>
    <div className="container h-screen w-full flex row justify-center items-center">
        <div className="bg-slate-500 px-8 py-12 rounded-xl">
            <div className="">
                <hr>
                <div className=" py-3">
                    <code>To implement Azure SSO in future</code>
                </div>
                <hr>
            </div>
            <div className="py-5">
                <div className=" flex row justify-center py-3">Temporary Login Mock-Up</div>
                <select id="roles" class="bg-gray-50 text-gray-900 text-sm rounded-lg block w-full p-3">
                    <option selected>Choose a role</option>
                    <option value="staff">Staff</option>
                    <option value="hr">Human Resources</option>
                    <option value="manager">Manager</option>
                </select>
            </div>
            <button className="bg-main text-slate-900 w-full mb-3">Login</button>
            <!-- <div v-for="user in this.users">{{ user[1] }}</div> -->

        </div>

    </div>
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