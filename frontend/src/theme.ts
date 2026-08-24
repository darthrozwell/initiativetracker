// src/theme.ts

import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
    palette: {
        mode: "dark",

        primary: {
            main: "#4CAF50",
        },

        secondary: {
            main: "#5C7CFA",
        },

        error: {
            main: "#D64545",
        },

        warning: {
            main: "#F0B429",
        },

        success: {
            main: "#4CAF50",
        },

        background: {
            default: "#1B1D22",
            paper: "#252830",
        },

        divider: "#3A3F4B",

        text: {
            primary: "#F3F4F6",
            secondary: "#A9AFB8",
        },
    },

    shape: {
        borderRadius: 10,
    },

    typography: {
        fontFamily: [
            "Inter",
            "Segoe UI",
            "Roboto",
            "Helvetica",
            "Arial",
            "sans-serif",
        ].join(","),

        h5: {
            fontWeight: 700,
        },

        h6: {
            fontWeight: 600,
        },

        subtitle1: {
            fontWeight: 600,
        },

        button: {
            textTransform: "none",
            fontWeight: 600,
        },
    },

    components: {
        MuiCssBaseline: {
            styleOverrides: {
                body: {
                    margin: 0,
                    padding: 0,
                    backgroundColor: "#1B1D22",
                },

                "#root": {
                    width: "100vw",
                    height: "100vh",
                    overflow: "hidden",
                },

                "*": {
                    boxSizing: "border-box",
                },

                "::-webkit-scrollbar": {
                    width: 8,
                    height: 8,
                },

                "::-webkit-scrollbar-track": {
                    background: "#252830",
                },

                "::-webkit-scrollbar-thumb": {
                    background: "#555B68",
                    borderRadius: 8,
                },

                "::-webkit-scrollbar-thumb:hover": {
                    background: "#6B7280",
                },
            },
        },

        MuiPaper: {
            defaultProps: {
                elevation: 0,
            },

            styleOverrides: {
                root: {
                    backgroundImage: "none",
                    border: "1px solid #3A3F4B",
                },
            },
        },

        MuiCard: {
            styleOverrides: {
                root: {
                    backgroundImage: "none",
                    border: "1px solid #3A3F4B",
                },
            },
        },

        MuiButton: {
            defaultProps: {
                disableElevation: true,
            },

            styleOverrides: {
                root: {
                    borderRadius: 8,
                    minHeight: 40,
                },
            },
        },

        MuiTabs: {
            styleOverrides: {
                root: {
                    minHeight: 48,
                },
            },
        },

        MuiTab: {
            styleOverrides: {
                root: {
                    minHeight: 48,
                },
            },
        },

        MuiLinearProgress: {
            styleOverrides: {
                root: {
                    height: 10,
                    borderRadius: 999,
                    backgroundColor: "#333843",
                },

                bar: {
                    borderRadius: 999,
                },
            },
        },

        MuiChip: {
            styleOverrides: {
                root: {
                    borderRadius: 8,
                },
            },
        },

        MuiAppBar: {
            styleOverrides: {
                root: {
                    backgroundImage: "none",
                    backgroundColor: "#252830",
                    borderBottom: "1px solid #3A3F4B",
                },
            },
        },

        MuiDivider: {
            styleOverrides: {
                root: {
                    borderColor: "#3A3F4B",
                },
            },
        },
    },
});