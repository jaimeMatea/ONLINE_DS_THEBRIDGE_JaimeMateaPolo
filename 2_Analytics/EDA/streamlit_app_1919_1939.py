########################### DASH ###########################

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output

# ==================================================
# 1. CARGA Y PREPARACIÓN DE LOS DATOS
# ==================================================

df = pd.read_csv(
    r"C:\Users\jaime\OneDrive\Documentos\GitHub\ONLINE_DS_THEBRIDGE_JaimeMateaPolo\2_Analytics\EDA\df_comparacion_peliculas.csv"
)

df = df.dropna(subset=[
    "country",
    "title",
    "year",
    "v2x_polyarchy",
    "political_instability_score"
])

df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["v2x_polyarchy"] = pd.to_numeric(
    df["v2x_polyarchy"], errors="coerce"
)
df["political_instability_score"] = pd.to_numeric(
    df["political_instability_score"], errors="coerce"
)

df = df.dropna(subset=[
    "year",
    "v2x_polyarchy",
    "political_instability_score"
])

paises = sorted(df["country"].unique())

colores = {
    "United States": "#3498DB",
    "Germany": "#E67E22",
    "United Kingdom": "#2ECC71"
}

# ==================================================
# 2. CONFIGURACIÓN DE DASH
# ==================================================

app = Dash(__name__)

app.title = "EL ESPEJO DEL MUNDO"

# ==================================================
# 3. ESTILOS GENERALES
# ==================================================

fondo = "#17212B"
panel = "#202D3A"
texto = "#F5F6FA"
secundario = "#AAB7B8"
amarillo = "#F1C40F"

estilo_grafico = {
    "paper_bgcolor": panel,
    "plot_bgcolor": panel,
    "font": {"color": texto, "family": "Arial"},
    "margin": {"l": 65, "r": 30, "t": 75, "b": 65},
    "legend": {"title": {"text": "País"}},
    "hoverlabel": {
        "bgcolor": fondo,
        "font_size": 13,
        "font_color": texto
    }
}

# ==================================================
# 4. COMPONENTES REUTILIZABLES
# ==================================================

def tarjeta_indicador(titulo, identificador, color):
    return html.Div(
        [
            html.P(
                titulo,
                style={
                    "color": secundario,
                    "fontSize": "14px",
                    "marginBottom": "8px"
                }
            ),
            html.H2(
                id=identificador,
                style={
                    "color": color,
                    "fontSize": "30px",
                    "margin": "0"
                }
            )
        ],
        style={
            "backgroundColor": panel,
            "padding": "20px",
            "borderRadius": "12px",
            "flex": "1",
            "minWidth": "180px",
            "border": "1px solid #34495E"
        }
    )


def estilo_tarjeta():
    return {
        "backgroundColor": panel,
        "padding": "20px",
        "borderRadius": "12px",
        "border": "1px solid #34495E"
    }


# ==================================================
# 5. ESTRUCTURA DEL DASHBOARD
# ==================================================

app.layout = html.Div(

    [

        # CABECERA
        html.Div(
            [
                html.H1(
                    "EL ESPEJO DEL MUNDO",
                    style={
                        "color": texto,
                        "fontSize": "34px",
                        "marginBottom": "5px"
                    }
                ),

                html.P(
                    "Cine, democracia e inestabilidad política "
                    "| Periodo 1919-1939",
                    style={
                        "color": secundario,
                        "fontSize": "16px"
                    }
                )
            ],
            style={
                "textAlign": "center",
                "padding": "25px"
            }
        ),

        # FILTROS
        html.Div(
            [

                html.Div(
                    [
                        html.Label(
                            "Países",
                            style={"color": texto}
                        ),

                        dcc.Dropdown(
                            id="filtro_paises",
                            options=[
                                {"label": p, "value": p}
                                for p in paises
                            ],
                            value=paises,
                            multi=True,
                            clearable=False,
                            style={"color": "#17212B"}
                        )
                    ],
                    style={"flex": "2", "minWidth": "250px"}
                ),

                html.Div(
                    [
                        html.Label(
                            "Periodo",
                            style={"color": texto}
                        ),

                        dcc.RangeSlider(
                            id="filtro_anios",
                            min=int(df["year"].min()),
                            max=int(df["year"].max()),
                            value=[
                                int(df["year"].min()),
                                int(df["year"].max())
                            ],
                            marks={
                                year: str(year)
                                for year in range(
                                    int(df["year"].min()),
                                    int(df["year"].max()) + 1,
                                    2
                                )
                            },
                            step=1,
                            tooltip={"placement": "bottom"}
                        )
                    ],
                    style={
                        "flex": "3",
                        "padding": "10px 20px"
                    }
                )

            ],
            style={
                "display": "flex",
                "gap": "30px",
                "alignItems": "center",
                "backgroundColor": panel,
                "padding": "25px",
                "borderRadius": "12px",
                "marginBottom": "25px",
                "flexWrap": "wrap"
            }
        ),

        # INDICADORES
        html.Div(
            [

                tarjeta_indicador(
                    "Películas analizadas",
                    "total_peliculas",
                    "#3498DB"
                ),

                tarjeta_indicador(
                    "Países seleccionados",
                    "total_paises",
                    "#2ECC71"
                ),

                tarjeta_indicador(
                    "Inestabilidad media",
                    "media_inestabilidad",
                    "#E67E22"
                ),

                tarjeta_indicador(
                    "Democracia media",
                    "media_democracia",
                    "#F1C40F"
                )

            ],
            style={
                "display": "flex",
                "gap": "15px",
                "flexWrap": "wrap",
                "marginBottom": "25px"
            }
        ),

        # PRIMERA FILA DE GRÁFICOS
        html.Div(
            [

                html.Div(
                    [
                        dcc.Graph(
                            id="grafico_democracia",
                            config={"displaylogo": False}
                        )
                    ],
                    style={
                        **estilo_tarjeta(),
                        "flex": "2",
                        "minWidth": "350px"
                    }
                ),

                html.Div(
                    [
                        dcc.Graph(
                            id="grafico_distribucion",
                            config={"displaylogo": False}
                        )
                    ],
                    style={
                        **estilo_tarjeta(),
                        "flex": "1",
                        "minWidth": "300px"
                    }
                )

            ],
            style={
                "display": "flex",
                "gap": "20px",
                "flexWrap": "wrap",
                "marginBottom": "20px"
            }
        ),

        # SEGUNDA FILA
        html.Div(
            [
                dcc.Graph(
                    id="grafico_temporal",
                    config={"displaylogo": False}
                )
            ],
            style={
                **estilo_tarjeta(),
                "marginBottom": "20px"
            }
        ),

        # TABLA
        html.Div(
            [
                html.H3(
                    "Películas seleccionadas",
                    style={"color": texto}
                ),

                html.Div(
                    id="tabla_peliculas"
                )
            ],
            style=estilo_tarjeta()
        )

    ],

    style={
        "backgroundColor": fondo,
        "minHeight": "100vh",
        "padding": "25px",
        "fontFamily": "Arial"
    }
)


# ==================================================
# 6. CALLBACK: ACTUALIZAR TODO EL DASHBOARD
# ==================================================

@app.callback(

    Output("total_peliculas", "children"),
    Output("total_paises", "children"),
    Output("media_inestabilidad", "children"),
    Output("media_democracia", "children"),

    Output("grafico_democracia", "figure"),
    Output("grafico_distribucion", "figure"),
    Output("grafico_temporal", "figure"),

    Output("tabla_peliculas", "children"),

    Input("filtro_paises", "value"),
    Input("filtro_anios", "value")

)


def actualizar_dashboard(paises_seleccionados, anios):

    # ----------------------------------------------
    # FILTRAR DATOS
    # ----------------------------------------------

    datos = df[
        (df["country"].isin(paises_seleccionados))
        &
        (df["year"].between(anios[0], anios[1]))
    ].copy()

    # ----------------------------------------------
    # INDICADORES
    # ----------------------------------------------

    total = datos["title"].nunique()

    numero_paises = datos["country"].nunique()

    media_inestabilidad = datos[
        "political_instability_score"
    ].mean()

    media_democracia = datos[
        "v2x_polyarchy"
    ].mean()

    # ----------------------------------------------
    # GRÁFICO 1: DEMOCRACIA E INESTABILIDAD
    # ----------------------------------------------

    fig_democracia = px.scatter(

        datos,

        x="v2x_polyarchy",
        y="political_instability_score",

        color="country",

        hover_name="title",

        hover_data={
            "country": True,
            "year": True,
            "v2x_polyarchy": ":.3f",
            "political_instability_score": True
        },

        color_discrete_map=colores,

        title="Democracia e inestabilidad política",

        labels={
            "v2x_polyarchy": "Índice de democracia electoral",
            "political_instability_score": "Inestabilidad política (0-5)",
            "country": "País"
        },

        opacity=0.8
    )

    fig_democracia.update_traces(
        marker={
            "size": 13,
            "line": {"width": 1, "color": "#FFFFFF"}
        }
    )

    fig_democracia.update_layout(
        **estilo_grafico,
        xaxis={"range": [-0.05, 1.05]},
        yaxis={"range": [-0.3, 5.4]}
    )

    # Zonas de referencia
    fig_democracia.add_vrect(
        x0=0,
        x1=0.3,
        fillcolor="#E74C3C",
        opacity=0.08,
        line_width=0
    )

    fig_democracia.add_vrect(
        x0=0.7,
        x1=1,
        fillcolor="#2ECC71",
        opacity=0.06,
        line_width=0
    )

    fig_democracia.add_hline(
        y=2.5,
        line_dash="dash",
        line_color="#F1C40F",
        line_width=2
    )

    # ----------------------------------------------
    # GRÁFICO 2: DISTRIBUCIÓN DE PUNTUACIONES
    # ----------------------------------------------

    fig_distribucion = px.box(

        datos,

        x="country",
        y="political_instability_score",

        color="country",

        points="all",

        color_discrete_map=colores,

        hover_data=["title", "year"],

        title="Distribución de la inestabilidad política",

        labels={
            "country": "País",
            "political_instability_score": "Puntuación (0-5)"
        }
    )

    fig_distribucion.update_layout(**estilo_grafico)

    # ----------------------------------------------
    # GRÁFICO 3: EVOLUCIÓN TEMPORAL
    # ----------------------------------------------

    datos_anuales = (
        datos
        .groupby(["country", "year"], as_index=False)
        ["political_instability_score"]
        .mean()
    )

    fig_temporal = px.line(

        datos_anuales,

        x="year",
        y="political_instability_score",

        color="country",

        markers=True,

        color_discrete_map=colores,

        title="Evolución anual de la inestabilidad política representada",

        labels={
            "year": "Año",
            "political_instability_score": "Inestabilidad media (0-5)",
            "country": "País"
        }
    )

    fig_temporal.update_layout(**estilo_grafico)

    fig_temporal.update_traces(
        marker={"size": 9},
        line={"width": 3}
    )

    # ----------------------------------------------
    # TABLA DE PELÍCULAS
    # ----------------------------------------------

    tabla = html.Div(

        [

            html.Table(

                [

                    html.Thead(
                        html.Tr(
                            [
                                html.Th("Película"),
                                html.Th("País"),
                                html.Th("Año"),
                                html.Th("Democracia"),
                                html.Th("Inestabilidad")
                            ]
                        )
                    ),

                    html.Tbody(

                        [

                            html.Tr(
                                [
                                    html.Td(fila["title"]),
                                    html.Td(fila["country"]),
                                    html.Td(int(fila["year"])),
                                    html.Td(
                                        f"{fila['v2x_polyarchy']:.3f}"
                                    ),
                                    html.Td(
                                        fila["political_instability_score"]
                                    )
                                ]
                            )

                            for _, fila in datos.head(100).iterrows()

                        ]

                    )

                ],

                style={
                    "width": "100%",
                    "borderCollapse": "collapse",
                    "color": texto,
                    "textAlign": "left"
                }

            ),

            html.P(
                f"Mostrando hasta 100 registros de {len(datos)} "
                "observaciones país-película.",
                style={"color": secundario}
            )

        ]

    )

    # ----------------------------------------------
    # DEVOLVER RESULTADOS
    # ----------------------------------------------

    return (

        f"{total:,}",
        str(numero_paises),
        f"{media_inestabilidad:.2f} / 5",
        f"{media_democracia:.3f}",

        fig_democracia,
        fig_distribucion,
        fig_temporal,

        tabla

    )


# ==================================================
# 7. EJECUTAR APLICACIÓN
# ==================================================

if __name__ == "__main__":
    app.run(debug=True)





































########################### STREAMLIT ###########################
# import streamlit as st
# import pandas as pd
# # --------------------------------------------------
# # CONFIGURACIÓN
# # --------------------------------------------------

# st.set_page_config(
#     page_title="El espejo del mundo",
#     page_icon="🎬",
#     layout="wide"
# )

# # --------------------------------------------------
# # CARGA DE DATOS
# # --------------------------------------------------

# @st.cache_data
# def cargar_datos():
#     return pd.read_csv("df_comparacion_peliculas.csv")

# df = cargar_datos()

# # --------------------------------------------------
# # TÍTULO
# # --------------------------------------------------

# st.title("🎬 EL ESPEJO DEL MUNDO")
# st.subheader("Cine, sociedad y contexto histórico (1919-1939)")

# st.markdown("""
# Explora la relación entre los problemas sociales de entreguerras
# y su representación en el cine de Estados Unidos, Alemania y Reino Unido.
# """)

# st.divider()

# # --------------------------------------------------
# # FILTROS LATERALES
# # --------------------------------------------------

# st.sidebar.header("Filtros")

# paises = sorted(df["country"].dropna().unique())

# paises_seleccionados = st.sidebar.multiselect(
#     "Selecciona los países",
#     options=paises,
#     default=paises
# )

# anios = sorted(df["year"].dropna().unique())

# anios_seleccionados = st.sidebar.slider(
#     "Periodo de estreno",
#     min_value=int(min(anios)),
#     max_value=int(max(anios)),
#     value=(int(min(anios)), int(max(anios)))
# )

# # Aplicar filtros
# df_filtrado = df[
#     (df["country"].isin(paises_seleccionados)) &
#     (df["year"].between(
#         anios_seleccionados[0],
#         anios_seleccionados[1]
#     ))
# ]

# st.write(f"Películas analizadas: **{len(df_filtrado)}**")

# st.divider()

# # --------------------------------------------------
# # PESTAÑAS
# # --------------------------------------------------

# tab1, tab2 = st.tabs([
#     "📉 Pobreza y economía",
#     "🏛️ Inestabilidad política y democracia"
# ])

# # --------------------------------------------------
# # GRÁFICO 1: POBREZA Y PIB
# # --------------------------------------------------

# with tab1:

#     st.header("Pobreza representada en el cine frente al PIB")

#     fig_pobreza = px.scatter(
#         df_filtrado,
#         x="GDP per capita",
#         y="poverty_score",
#         color="country",
#         hover_name="title",
#         hover_data={
#             "country": True,
#             "year": True,
#             "GDP per capita": ":,.0f",
#             "poverty_score": True
#         },
#         labels={
#             "GDP per capita": "PIB per cápita",
#             "poverty_score": "Puntuación de pobreza (0-5)",
#             "country": "País"
#         },
#         opacity=0.75
#     )

#     fig_pobreza.update_traces(
#         marker=dict(size=11),
#         hovertemplate=(
#             "<b>%{hovertext}</b><br>"
#             "País: %{customdata[0]}<br>"
#             "Año: %{customdata[1]}<br>"
#             "PIB per cápita: %{x:,.0f}<br>"
#             "Pobreza: %{y}"
#             "<extra></extra>"
#         )
#     )

#     fig_pobreza.update_layout(
#         height=600,
#         hoverlabel=dict(font_size=13),
#         legend_title="País"
#     )

#     st.plotly_chart(fig_pobreza, use_container_width=True)

#     st.markdown("""
#     **Interpretación:**

#     Cada punto representa una película. Su posición permite comparar
#     la intensidad de la representación de la pobreza con la situación
#     económica del país en el año de estreno.
#     """)

# # --------------------------------------------------
# # GRÁFICO 2: INESTABILIDAD Y DEMOCRACIA
# # --------------------------------------------------

# with tab2:

#     st.header("Inestabilidad política representada en el cine frente a la democracia")

#     fig_politica = px.scatter(
#         df_filtrado,
#         x="v2x_polyarchy",
#         y="political_instability_score",
#         color="country",
#         hover_name="title",
#         hover_data={
#             "country": True,
#             "year": True,
#             "v2x_polyarchy": ":.3f",
#             "political_instability_score": True
#         },
#         labels={
#             "v2x_polyarchy": "Índice de democracia electoral",
#             "political_instability_score": "Puntuación de inestabilidad política (0-5)",
#             "country": "País"
#         },
#         opacity=0.75
#     )

#     fig_politica.update_traces(
#         marker=dict(size=11),
#         hovertemplate=(
#             "<b>%{hovertext}</b><br>"
#             "País: %{customdata[0]}<br>"
#             "Año: %{customdata[1]}<br>"
#             "Democracia electoral: %{x:.3f}<br>"
#             "Inestabilidad política: %{y}"
#             "<extra></extra>"
#         )
#     )

#     fig_politica.update_layout(
#         height=600,
#         hoverlabel=dict(font_size=13),
#         legend_title="País"
#     )

#     st.plotly_chart(fig_politica, use_container_width=True)

#     st.markdown("""
#     **Interpretación:**

#     Cada punto representa una película. Se compara su puntuación de
#     inestabilidad política con el nivel de democracia electoral
#     del país en el año de estreno.
#     """)

# # --------------------------------------------------
# # TABLA DE DATOS
# # --------------------------------------------------

# with st.expander("Consultar los datos utilizados"):

#     st.dataframe(
#         df_filtrado,
#         use_container_width=True
#     )
