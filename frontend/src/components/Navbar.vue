<template>
    <div class="flex md:hidden">
        <div class="navbar navbar-dark px-4 bg-navbar container-fluid">
            <div class="flex flex-row justify-between w-full">
                <button class="navbar-toggler border-none p-0" type="button" data-bs-toggle="offcanvas"
                    data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="offcanvas offcanvas-start h-screen w-56 bg-navbar" id="menu">
                    <div class="px-4 py-2 h-full">
                        <button class="navbar-toggler border-none px-0 py-[5px]" type="button" data-bs-toggle="offcanvas"
                            data-bs-target="#menu" aria-controls="menu" aria-expanded="false"
                            aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <!-- Side NavBar content -->
                        <div class="pt-6 flex flex-col gap-2">
                            <div class="p-2">
                                <div v-if="true" class="text-white cursor-pointer" @click="handleHome()"
                                    data-bs-toggle="offcanvas" data-bs-target="#menu">Home
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Profile -->
                <div class="user" type="button" data-bs-toggle="dropdown">
                    <div class="px-3 py-2 bg-avatar rounded-full">
                        <span class="initials text-dark">{{ user.fName.slice(0, 1) }} {{ user.lName.slice(0,
                            1)
                        }}</span>
                    </div>
                </div>
                <ul class="dropdown-menu dropdown-menu-end">
                    <li><a class="dropdown-item" @click="handleProfile">Profile</a></li>
                    <li><a class="dropdown-item" @click="handleLogout">Log out</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="hidden md:flex">
        <div class="navbar navbar-dark px-4 bg-navbar text-white container-fluid">
            <div class="logo flex items-center cursor-pointer" @click="handleHome()">
                <img src="/portal.png" width="40" height="40" />
                <div class="ml-3 text-h1">Skill Based Role Portal</div>
            </div>
            <div class="flex">
                <!-- Links -->
                <div class="flex items-center justify-between pr-8">
                    <!-- Admin -->
                    <a v-if="user.accessRights == 0">admin link</a>
                    <!-- Staff -->
                    <a v-if="user.accessRights == 1">staff link</a>
                    <!-- Manager -->
                    <a v-if="user.accessRights == 2">manager link</a>
                </div>
                <!-- Dev panel -->
                <div @mouseover="showDevPanel = true" @mouseleave="showDevPanel = false" class="pr-8 flex items-center">
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
                <!-- Profile -->
                <div class="user" type="button" data-bs-toggle="dropdown">
                    <div class="px-3 py-2 bg-avatar rounded-full">
                        <span class="initials text-dark">{{ user.fName.slice(0, 1) }} {{ user.lName.slice(0,
                            1)
                        }}</span>
                    </div>
                </div>
                <ul class="dropdown-menu dropdown-menu-end">
                    <li><a class="dropdown-item" @click="handleProfile">Profile</a></li>
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
    },
    methods: {
        handleLogout() {
            sessionStorage.clear();
            window.location.href = "/";
            //this.$router.push({ name: "Login" })
        },
        handleHome() {
            this.$router.push({ name: "Home" })
        },
        handleProfile() {
            console.log("not yet implemented")
        }
    }
}
</script>