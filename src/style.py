import gradio as gr

theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="blue",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
)

css = """
.gradio-container {
    max-width: 820px !important;
    margin: auto !important;
}
#twin-header {
    text-align: center;
    margin-bottom: 0.5rem;
}
#twin-header h1 {
    margin-bottom: 0.15rem;
}
#twin-header p {
    color: var(--body-text-color-subdued);
    margin-top: 0;
}
"""
