/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	theme: {
		extend: {
			colors: {
				main: "#D5BDAF",
				accent: "#F5EBE0",
				sec: "#E3D5CA",
				"accent-hover": "#977D35",
				"accent-hover-outlined": "#EADFC3",
				"accent-secondary": "#EAE0C3",
				paper: "#3C3115",
			},
		},
	},
	plugins: [],
};
