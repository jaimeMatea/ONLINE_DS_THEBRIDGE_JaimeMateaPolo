import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output


# =====================================================
# 1. CONFIGURACIÓN
# =====================================================

paises = [
    "Italy",
    "Japan",
    "France",
    "United States"
]

variables = [
    "war_score",
    "poverty_score",
    "political_repression_score",
    "nuclear_fear_score",
    "trauma_score"
]

nombres_variables = {
    "war_score": "Guerra",
    "poverty_score": "Pobreza",
    "political_repression_score": "Represión política",
    "nuclear_fear_score": "Miedo nuclear",
    "trauma_score": "Trauma"
}


# =====================================================
# 2. PREPARACIÓN DE LOS DATOS
# =====================================================

# Directorio donde está este archivo app_1940_1960.py
BASE_DIR = Path(__file__).resolve().parent

# Cargar los CSV desde esa misma carpeta
df_peliculas_dash = pd.read_csv(
    BASE_DIR / "peliculas_1940_1960_clasificado.csv"
)

df_social_dash = pd.read_csv(
    BASE_DIR / "df_social_1940_1960.csv"
)

# Separamos los países de producción
df_peliculas_dash["country"] = (
    df_peliculas_dash["paises_norm"]
    .fillna("")
    .str.split(",")
)

df_peliculas_dash = df_peliculas_dash.explode("country")

df_peliculas_dash["country"] = (
    df_peliculas_dash["country"].str.strip()
)

df_peliculas_dash = df_peliculas_dash[
    df_peliculas_dash["country"].isin(paises)
].copy()

# Preparamos el año
df_peliculas_dash["release_year"] = pd.to_numeric(
    df_peliculas_dash["release_year"],
    errors="coerce"
)

df_peliculas_dash = df_peliculas_dash.dropna(
    subset=["release_year"]
)

df_peliculas_dash["year"] = (
    df_peliculas_dash["release_year"].astype(int)
)

# Preparamos los datos sociales
df_social_dash["year"] = pd.to_numeric(
    df_social_dash["year"],
    errors="coerce"
)

df_social_dash = df_social_dash.dropna(
    subset=["year", "country"]
)

df_social_dash["year"] = df_social_dash["year"].astype(int)

df_social_dash["country"] = (
    df_social_dash["country"].str.strip()
)

df_social_dash = df_social_dash[
    df_social_dash["country"].isin(paises)
].copy()

# Unimos películas y datos sociales
df_completo_dash = df_peliculas_dash.merge(
    df_social_dash,
    on=["country", "year"],
    how="left"
)


# =====================================================
# 3. AGREGACIONES
# =====================================================

# Agrupación de las puntuaciones cinematográficas por país y año
df_cine_anual = (
    df_completo_dash
    .groupby(["country", "year"], as_index=False)
    .agg(
        war_score=("war_score", "mean"),
        poverty_score=("poverty_score", "mean"),
        political_repression_score=(
            "political_repression_score", "mean"
        ),
        nuclear_fear_score=("nuclear_fear_score", "mean"),
        trauma_score=("trauma_score", "mean"),
        num_movies=("title", "nunique")
    )
)

# Indicadores sociales por país y año
df_social_anual = (
    df_social_dash
    .groupby(["country", "year"], as_index=False)
    .agg(
        life_expectancy=("life_expectancy", "first"),
        infant_mortality=("infant_mortality", "first"),
        military_deaths=("military_deaths", "first"),
        civilian_deaths_min=("civilian_deaths_min", "first"),
        civilian_deaths_max=("civilian_deaths_max", "first")
    )
)

# Unimos los datos anuales
df_anual = df_cine_anual.merge(
    df_social_anual,
    on=["country", "year"],
    how="left"
)


# =====================================================
# 4. PREPARAR TIPOS DE REPRESENTACIÓN
# =====================================================

df_representation = df_peliculas_dash.copy()

# =====================================================
# 5. CREAR LA APLICACIÓN DASH
# =====================================================

app = Dash(__name__)

app.title = "El espejo del mundo | 1940-1960"


# =====================================================
# 6. DISEÑO DEL DASHBOARD
# =====================================================

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f5f7",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        # CABECERA
        html.Div(
            style={
                "backgroundColor": "#172337",
                "padding": "30px",
                "borderRadius": "12px",
                "color": "white",
                "marginBottom": "25px"
            },
            children=[
                html.H1(
                    "EL ESPEJO DEL MUNDO",
                    style={
                        "marginBottom": "5px",
                        "fontSize": "32px"
                    }
                ),

                html.H3(
                    "El cine y la realidad histórica (1940-1960)",
                    style={
                        "fontWeight": "normal",
                        "color": "#cbd5e1"
                    }
                ),

                html.P(
                    "Análisis de la representación cinematográfica "
                    "de la guerra, la pobreza, la represión, el trauma "
                    "y el miedo nuclear en cuatro países.",
                    style={
                        "fontSize": "15px",
                        "color": "#dbe3ed"
                    }
                )
            ]
        ),

        # FILTRO DE PAÍSES
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.Label(
                    "Selecciona los países:",
                    style={"fontWeight": "bold"}
                ),

                dcc.Dropdown(
                    id="filtro-paises",
                    options=[
                        {"label": p, "value": p}
                        for p in paises
                    ],
                    value=paises,
                    multi=True,
                    clearable=False
                )
            ]
        ),

        # TARJETAS KPI
        html.Div(
            id="kpis",
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "15px",
                "marginBottom": "25px"
            }
        ),

        # GRÁFICO 1
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.H3(
                    "1. Trauma cinematográfico y esperanza de vida"
                ),

                dcc.Graph(id="grafico-trauma")
            ]
        ),

        # GRÁFICO 2
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.H3(
                    "2. Evolución de las temáticas cinematográficas"
                ),

                dcc.Graph(id="grafico-tematicas")
            ]
        ),

        # GRÁFICO 3
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.H3(
                    "3. Mortalidad infantil y representación de la pobreza"
                ),

                dcc.Graph(id="grafico-pobreza")
            ]
        ),

        # GRÁFICO 4
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.H3(
                    "4. Tipos de representación cinematográfica"
                ),

                dcc.Graph(id="grafico-representacion")
            ]
        ),

        # GRÁFICO 5
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "marginBottom": "25px"
            },
            children=[
                html.H3(
                    "5. Evolución del miedo nuclear"
                ),

                dcc.Graph(id="grafico-nuclear")
            ]
        )
    ]
)


# =====================================================
# 7. CALLBACK
# =====================================================

@app.callback(
    Output("kpis", "children"),
    Output("grafico-trauma", "figure"),
    Output("grafico-tematicas", "figure"),
    Output("grafico-pobreza", "figure"),
    Output("grafico-representacion", "figure"),
    Output("grafico-nuclear", "figure"),

    Input("filtro-paises", "value")
)


def actualizar_dashboard(paises_seleccionados):

    if not paises_seleccionados:
        paises_seleccionados = paises

    df = df_completo_dash[
        df_completo_dash["country"].isin(paises_seleccionados)
    ].copy()

    df_anual_filtrado = df_anual[
        df_anual["country"].isin(paises_seleccionados)
    ].copy()

    df_rep = df_representation[
        df_representation["country"].isin(paises_seleccionados)
    ].copy()


    # =================================================
    # KPI
    # =================================================

    total_peliculas = df_rep["title"].nunique()

    media_trauma = df["trauma_score"].mean()

    media_guerra = df["war_score"].mean()

    media_nuclear = df["nuclear_fear_score"].mean()


    def crear_kpi(titulo, valor):

        return html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "textAlign": "center",
                "boxShadow": "0 2px 5px rgba(0,0,0,0.05)"
            },

            children=[
                html.P(
                    titulo,
                    style={
                        "color": "#64748b",
                        "fontSize": "14px"
                    }
                ),

                html.H2(
                    valor,
                    style={
                        "color": "#172337",
                        "margin": "0"
                    }
                )
            ]
        )


    kpis = [
        crear_kpi(
            "Películas analizadas",
            f"{total_peliculas:,}"
        ),

        crear_kpi(
            "Trauma medio",
            f"{media_trauma:.2f}" if pd.notna(media_trauma) else "N/D"
        ),

        crear_kpi(
            "Guerra media",
            f"{media_guerra:.2f}" if pd.notna(media_guerra) else "N/D"
        ),

        crear_kpi(
            "Miedo nuclear medio",
            f"{media_nuclear:.2f}" if pd.notna(media_nuclear) else "N/D"
        )
    ]


    # =================================================
    # GRÁFICO 1: TRAUMA Y ESPERANZA DE VIDA
    # =================================================

    df_trauma = (
        df.groupby(["country", "year"], as_index=False)
        .agg(
            trauma_score=("trauma_score", "mean")
        )
    )

    df_trauma = df_trauma.merge(
        df_social_anual[
            ["country", "year", "life_expectancy"]
        ],
        on=["country", "year"],
        how="left"
    )

    fig1 = make_subplots(
        specs=[[{"secondary_y": True}]]
    )

    for pais in paises_seleccionados:

        datos = df_trauma[
            df_trauma["country"] == pais
        ]

        fig1.add_trace(
            go.Scatter(
                x=datos["year"],
                y=datos["trauma_score"],
                name=f"{pais} - Trauma",
                mode="lines+markers"
            ),
            secondary_y=False
        )

        fig1.add_trace(
            go.Scatter(
                x=datos["year"],
                y=datos["life_expectancy"],
                name=f"{pais} - Esperanza de vida",
                mode="lines",
                line={"dash": "dash"}
            ),
            secondary_y=True
        )

    fig1.update_layout(
        template="plotly_white",
        hovermode="x unified",
        legend_title="País y variable"
    )

    fig1.update_xaxes(title_text="Año")

    fig1.update_yaxes(
        title_text="Trauma cinematográfico (0-5)",
        secondary_y=False
    )

    fig1.update_yaxes(
        title_text="Esperanza de vida (años)",
        secondary_y=True
    )


    # =================================================
    # GRÁFICO 2: EVOLUCIÓN DE LAS TEMÁTICAS
    # =================================================

    df_tematicas = (
        df.groupby(["country", "year"], as_index=False)[variables]
        .mean()
    )

    df_tematicas = df_tematicas.melt(
        id_vars=["country", "year"],
        value_vars=variables,
        var_name="tematica",
        value_name="puntuacion"
    )

    df_tematicas["tematica"] = (
        df_tematicas["tematica"]
        .map(nombres_variables)
    )

    fig2 = px.line(
        df_tematicas,
        x="year",
        y="puntuacion",
        color="tematica",
        facet_col="country",
        facet_col_wrap=2,
        markers=True,
        category_orders={
            "country": paises
        },
        labels={
            "year": "Año",
            "puntuacion": "Puntuación media (0-5)",
            "tematica": "Temática",
            "country": "País"
        }
    )

    fig2.update_layout(
        template="plotly_white",
        hovermode="x unified",
        legend_title="Temáticas"
    )

    fig2.update_yaxes(range=[0, 5])


    # =================================================
    # GRÁFICO 3: MORTALIDAD INFANTIL Y POBREZA
    # =================================================

    df_pobreza = (
        df.groupby(["country", "year"], as_index=False)
        .agg(
            poverty_score=("poverty_score", "mean"),
            num_movies=("title", "nunique")
        )
    )

    df_pobreza = df_pobreza.merge(
        df_social_anual[
            ["country", "year", "infant_mortality"]
        ],
        on=["country", "year"],
        how="left"
    )

    df_pobreza = df_pobreza.dropna(
        subset=["poverty_score", "infant_mortality"]
    )

    fig3 = px.scatter(
        df_pobreza,
        x="infant_mortality",
        y="poverty_score",
        color="country",
        size="num_movies",
        hover_data=["year", "num_movies"],
        labels={
            "infant_mortality": "Mortalidad infantil",
            "poverty_score": "Puntuación de pobreza (0-5)",
            "country": "País",
            "num_movies": "Películas"
        }
    )

    fig3.update_layout(
        template="plotly_white"
    )

    fig3.update_yaxes(range=[0, 5])


    # =================================================
    # GRÁFICO 4: TIPOS DE REPRESENTACIÓN
    # =================================================

    df_rep_anual = (
    df_rep.dropna(subset=["representation_type"])
    .groupby(["country", "representation_type"])["title"]
    .nunique()
    .reset_index(name="num_movies")
    )

    fig4 = px.bar(
        df_rep_anual,
        x="country",
        y="num_movies",
        color="representation_type",
        barmode="relative",
        labels={
            "country": "País",
            "num_movies": "Porcentaje de películas",
            "representation_type": "Tipo de representación"
        }
    )

    # Convertimos las barras a porcentajes
    fig4.update_layout(
        template="plotly_white",
        barnorm="percent",
        yaxis_title="Porcentaje (%)",
        legend_title="Tipo de representación"
    )


    # =================================================
    # GRÁFICO 5: MIEDO NUCLEAR
    # =================================================

    df_nuclear = (
        df.groupby(["country", "year"], as_index=False)
        .agg(
            nuclear_fear_score=("nuclear_fear_score", "mean")
        )
    )

    fig5 = px.line(
        df_nuclear,
        x="year",
        y="nuclear_fear_score",
        color="country",
        markers=True,
        labels={
            "year": "Año",
            "nuclear_fear_score": "Miedo nuclear (0-5)",
            "country": "País"
        }
    )

    fig5.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    fig5.update_yaxes(range=[0, 5])


    return kpis, fig1, fig2, fig3, fig4, fig5


# =====================================================
# 8. EJECUTAR DASHBOARD
# =====================================================

app.run(debug=True, jupyter_mode="external")