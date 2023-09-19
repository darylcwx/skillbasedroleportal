<template>
    <div class="container mx-auto max-w-lg h-screen flex row justify-center items-center">
        <div class="bg-ghost px-16 py-12 rounded-xl shadow-md shadow-slate-400">

            <div class="pb-4 text-h1">
                Sign in to your account
            </div>

            <div class="pb-4">
                <label for="email" class="form-label text-h3">Email</label>
                <select id="email" v-model="userEmail" class="w-full rounded-lg form-select" required>
                    <option selected>Choose a user</option>
                    <option v-for="user in users" :value="user.Email">
                        {{ user.Email }}
                    </option>

                </select>
                <div id="emailValidationHelper" class="invalid-feedback">
                    Please select a user
                </div>

            </div>
            <div class="pb-4">
                <div class="mb-3">
                    <label for="basic-url" class="form-label text-h3">Password</label>
                    <input type="text" disabled class="form-control is-valid" />
                    <div class="valid-feedback">
                        Disabled for mockup purposes
                    </div>
                </div>
            </div>

            <div class="">
                <button class="btn btn-primary w-full text-btn" v-on:click="handleLogin">
                    Login
                </button>
            </div>

            <div className="flex justify-center items-center py-4">
                <hr className="grow border-t-2 border-gray-500" />
                <div className="px-3 text-gray-500">or</div>
                <hr className="grow border-t-2 border-gray-500" />
            </div>

            <div class="">
                <button class="btn btn-primary w-full text-btn" v-on:click="handleSSO">
                    Sign in with single sign-on (SSO)
                </button>
            </div>
            <div v-if="showSSOError" class="absolute bottom-5 right-10">
                <div class="alert alert-info fade show" role="alert">
                    <h4 class="alert-heading">Oh no!</h4>
                    SSO will only be implemented in future sprints.
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { resolveTransitionHooks } from 'vue';

export default {
    data() {
        return {
            userEmail: "Choose a user",
            users: [],
            showSSOError: false,
            reload: true,
        };
    },
    created() { },

    mounted() {
        //console.log(this.$store.state.user);
        this.fetchUsers();

    },
    methods: {
        async fetchUsers() {
            try {
                const apiUrl = "http://localhost:5000/api/users";
                const response = await fetch(apiUrl);
                const data = await response.json();
                this.users = data.users
                console.log(this.users)
            } catch (error) {
                console.error(
                    "There was a problem with the fetch operation:",
                    error
                );
            }
        },
        async handleLogin() {
            document.getElementById("email").classList.remove('is-invalid');
            document.getElementById("emailValidationHelper").classList.remove('block');
            if (this.userEmail === "Choose a user") {
                document.getElementById("email").classList.add('is-invalid');
                document.getElementById("emailValidationHelper").classList.add('block');
                return;
            }
            try {
                const apiUrl = `http://localhost:5000/api/user?email=${encodeURIComponent(this.userEmail)}`;
                const response = await fetch(apiUrl);
                const data = await response.json();
                console.log(data)
                const user = data
                this.$store.commit('setUser', {
                    id: user.Staff_ID, fName: user.Staff_FName, lName: user.Staff_LName, dept: user.Dept, email: user.Email, accessRights: user.Access_Rights
                });
                this.$router.push({ name: "Home" });
            } catch (error) {
                console.error(
                    error
                );
            }

        },
        handleSSO() {
            this.showSSOError = true;
            setTimeout(() => { this.showSSOError = false; }, 5000)
        }

    },
};
</script>
