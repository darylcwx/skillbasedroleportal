<template>
    <div v-if="mobile">

    </div>
    <div v-if="true">
        <div class="fixed mx-auto bg-navbar text-white top-0 h-12 px-4 w-full flex col justify-between items-center">
            <div class="">Welcome Back, {{ user.fName }} {{ user.lName }}!</div>
            <div class="flex">
                <div @mouseover="showDevPanel = true" @mouseleave="showDevPanel = false" class="pr-4 flex items-center">
                    Dev
                    <div v-if="showDevPanel" class="absolute right-10 bg-zinc-600 p-4 rounded-lg top-10">
                        <span class="text-h3 text-lg">User details:</span><br>
                        accessRights: {{ user.accessRights == 0 ? "admin" : user.accessRights == 1 ? "user" : "manager"
                        }}<br>
                        userID: {{ user.id }}<br>
                        email: {{ user.email }}<br>
                        fName: {{ user.fName }}<br>
                        lName: {{ user.lName }}<br>
                        dept: {{ user.dept }}<br>
                    </div>
                </div>
                <div class="user" type="button" data-bs-toggle="dropdown">
                    <div class="px-3 py-2 bg-primary rounded-full">
                        <span class="initials">{{ user.fName.slice(0, 1) }} {{ user.lName.slice(0, 1) }}</span>
                    </div>
                </div>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="">Profile</a></li>
                    <li><a class="dropdown-item" @click="handleLogout">Log out</a></li>
                </ul>
            </div>
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