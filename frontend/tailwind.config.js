/** @type {import('tailwindcss').Config} */
export default {
	corePlugins: { preflight: false },
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	theme: {
		extend: {
			colors: {
				ghost: "#F2F4FF",
				alice: "#EAF6FF",
				oxford: "#0B132B",
				snow: "#F6F4F3",
				cadet: "#1C2541",
				main: "#D5BDAF",
				accent: "#F5EBE0",
				sec: "#E3D5CA",
				"accent-hover": "#977D35",
				"accent-hover-outlined": "#EADFC3",
				"accent-secondary": "#EAE0C3",
				paper: "#3C3115",
			},
			fontSize: {
				xs: ".75rem", // Extra small font size
				sm: ".875rem", // Small font size
				base: "1rem", // Base font size
				lg: "1.125rem", // Large font size
				xl: "1.25rem", // Extra large font size
				"2xl": "1.5rem", // 2x large font size
				"3xl": "1.875rem", // 3x large font size
				"4xl": "2.25rem", // 4x large font size
				"5xl": "3rem", // 5x large font size
				"6xl": "4rem", // 6x large font size
			},
			fontWeight: {
				thin: "100", // Thin font weight
				extralight: "200", // Extra-light font weight
				light: "300", // Light font weight
				normal: "400", // Normal font weight
				medium: "500", // Medium font weight
				semibold: "600", // Semi-bold font weight
				bold: "700", // Bold font weight
				extrabold: "800", // Extra-bold font weight
				black: "900", // Black font weight
			},
		},
	},
	important: true,
	plugins: [],
};
