import streamlit as st
from streamlit_elements import elements, mui, dashboard
import base64
from io import BytesIO


def image_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# Load and convert images to base64
protein_calc_img = image_to_base64("./img/st_protein_calc.png")
lottery_heatmap_img = image_to_base64("./img/st_lottery_heatmap.png")
market_matrix_img = image_to_base64("./img/st_market_matrix.png")
csv_explorer_img = image_to_base64("./img/st_csv_explorer.png")

st.title("Streamlit Doodles")

with st.container():
    st.write(
        "This is a simple Streamlit app to showcase a number of other Streamlit apps that I've built with Cursor.ai"
    )
    st.write("More about me at [scottgoley.com](https://scottgoley.com/)")

    st.write("---")

    with elements("dashboard"):
        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("app1", 0, 0, 2, 3),
            dashboard.Item("app2", 2, 0, 2, 3),
            dashboard.Item("app3", 0, 2, 2, 3),
            dashboard.Item("app4", 2, 2, 2, 3),
            dashboard.Item("app5", 0, 4, 2, 3),
        ]

        with dashboard.Grid(layout):
            with mui.Card(key="app1", sx={"height": "100%"}):
                mui.CardMedia(
                    component="img",
                    height="140",
                    image=f"data:image/png;base64,{protein_calc_img}",
                    alt="Protein Calculator thumbnail",
                )
                mui.CardContent(
                    mui.Typography("Streamlit App 1: Protein Calculator", variant="h6"),
                    mui.Typography(
                        "This app allows you to calculate your target daily protein intake as well as understand the foods, quantities, and costs associated with meeting that target.",
                        sx={"mb": 2},
                    ),
                    mui.Button(
                        "Launch Protein Calculator",
                        href="https://sg-protein-calc.streamlit.app/",
                        target="_blank",
                    ),
                )

            with mui.Card(key="app2", sx={"height": "100%"}):
                mui.CardMedia(
                    component="img",
                    height="140",
                    image=f"data:image/png;base64,{lottery_heatmap_img}",
                    alt="Lottery Heatmap thumbnail",
                )
                mui.CardContent(
                    mui.Typography("Streamlit App 2: Lottery Heatmap", variant="h6"),
                    mui.Typography(
                        "This app allows you to explore the historical data of either the Powerball or Mega Millions lottery.",
                        sx={"mb": 2},
                    ),
                    mui.Button(
                        "Launch Lottery Heatmap",
                        href="https://sg-lottery-heatmap.streamlit.app/",
                        target="_blank",
                    ),
                )

            with mui.Card(key="app3", sx={"height": "100%"}):
                mui.CardMedia(
                    component="img",
                    height="140",
                    image=f"data:image/png;base64,{market_matrix_img}",
                    alt="CSV Explorer thumbnail",
                )
                mui.CardContent(
                    mui.Typography("Streamlit App 3: Market Matrix", variant="h6"),
                    mui.Typography(
                        """This app illustrates the performance of the S&P 500
                        over the long term and the convergence to its long term
                        return regardless of starting period.""",
                        sx={"mb": 2},
                    ),
                    mui.Button(
                        "Launch Market Matrix",
                        href="https://sg-market-matrix.streamlit.app/",
                        target="_blank",
                    ),
                )

            with mui.Card(key="app4", sx={"height": "100%"}):
                mui.CardMedia(
                    component="img",
                    height="140",
                    image=f"data:image/png;base64,{csv_explorer_img}",
                    alt="CSV Explorer thumbnail",
                )
                mui.CardContent(
                    mui.Typography("Streamlit App 4: CSV Explorer", variant="h6"),
                    mui.Typography(
                        "This app allows you to explore a CSV file with autogenerated filters based on the upload's content.",
                        sx={"mb": 2},
                    ),
                    mui.Button(
                        "Launch CSV Explorer",
                        href="https://sg-csv-explorer.streamlit.app/",
                        target="_blank",
                    ),
                )

            with mui.Card(key="app5", sx={"height": "100%"}):
                mui.CardContent(
                    mui.Typography("Streamlit App 5: GFC Explorer", variant="h6"),
                    mui.Typography(
                        "This app allows you to explore the Home Price Index dataset from The Federal Housing Finance Agency see that data visualized a few different ways.",
                        sx={"mb": 2},
                    ),
                    mui.Button(
                        "Launch GFC Explorer",
                        href="https://sg-gfc-explorer.streamlit.app/",
                        target="_blank",
                    ),
                )

        def handle_layout_change(updated_layout):
            print(updated_layout)

    st.write("---")
