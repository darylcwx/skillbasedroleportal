<template>
    <div className="flex justify-between bg-slate-800">
        <div className="p-4 hover:scale-150 transition duration-150 ease-in-out">Logo here</div>
        <div className="flex row gap-2 px-4">
            <div className="p-4">
                <router-link to="/">Home</router-link>
            </div>
            <div className="p-4">
                <router-link to="/skills" className="p-4">Skills</router-link>
            </div>
        </div>
    </div>
</template>