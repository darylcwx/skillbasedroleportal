<template>
    <div class="fixed mx-auto bg-slate-700 text-white top-0 h-12 px-8 w-full flex col justify-between items-center">
        <div class="">Welcome Back, {{ user.fName }} {{ user.lName }}!</div>
        <div class="flex">
            <div @mouseover="showDevPanel = true" @mouseleave="showDevPanel = false" class="pr-4">
                For Development
                <div v-if="showDevPanel" class="absolute right-10 bg-zinc-600 p-4 rounded-lg mt-2">
                    <span class="text-h3 text-lg">User details:</span><br>
                    accessRights: {{ user.accessRights == 0 ? "admin" : user.accessRights == 1 ? "user" : "manager" }}<br>
                    userID: {{ user.id }}<br>
                    email: {{ user.email }}<br>
                    fName: {{ user.fName }}<br>
                    lName: {{ user.lName }}<br>
                    dept: {{ user.dept }}<br>
                </div>
            </div>
            <a class="" @click="handleLogout">Log out</a>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            user: this.$store.state.user,
            showDevPanel: false,
        };
    },
    created() {

    },
    mounted() {
        console.log(this.user)
    },
    methods: {
        handleLogout() {
            sessionStorage.clear();
            window.location.href = "/";
            //this.$router.push({ name: "Login" })
        }
    }
}
</script>