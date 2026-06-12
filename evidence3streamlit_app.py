import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página (Modo Ancho para simular una lona infográfica)
st.set_page_config(
    page_title="NYZ Logy 2050 - Cuadro de Mando Integral",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------
# DISEÑO VISUAL INYECTADO (Estilos CSS personalizados para tipografías gigantes y colores vivos)
# -------------------------------------------------------------
st.markdown("""
<style>
    /* Estilos globales */
    .title-banner {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .title-banner h1 {
        font-size: 50px !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }
    .title-banner p {
        font-size: 20px !important;
    }
    
    /* Encabezados de sección tipo Infografía */
    .section-header {
        background-color: #f1f5f9;
        padding: 12px 20px;
        border-radius: 8px;
        border-left: 8px solid #2563eb;
        font-size: 26px !important;
        font-weight: 700;
        color: #1e293b;
        margin-top: 35px;
        margin-bottom: 20px;
    }
    
    /* Tarjetas de Datos de Alto Impacto */
    .kpi-card {
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .fin-card { background: linear-gradient(135deg, #b91c1c 0%, #ef4444 100%); }      /* Rojo Intenso */
    .cli-card { background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%); }      /* Turquesa/Teal */
    .proc-card { background: linear-gradient(135deg, #059669 0%, #10b981 100%); }     /* Verde Esmeralda */
    .cap-card { background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%); }      /* Ámbar/Naranja */
    
    .kpi-card h3 { font-size: 18px !important; margin-bottom: 8px !important; opacity: 0.9; font-weight: 600; text-transform: uppercase; }
    .kpi-card .value { font-size: 42px !important; font-weight: 800; margin-bottom: 5px; }
    .kpi-card .meta { font-size: 14px !important; opacity: 0.85; font-style: italic; }
    
    /* Tarjetas de Información en Sidebar */
    .sidebar-box {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }
    .sidebar-box h4 { color: #1e3a8a; font-weight: 700; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# BARRA LATERAL (PORTADA E IDENTIDAD INSTITUCIONAL)
# -------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎓 Evidencia Final")
    st.markdown("**Curso:** Strategic Thinking\n\n**Profesor:** José Guillermo Ituarte Marumoto")
    
    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 👥 Equipo de Consultores")
    st.markdown("""
    <div class='sidebar-box'>
        <p style='margin-bottom:5px; font-weight:600;'>• Diego Arnulfo Márquez H.</p>
        <p style='margin-bottom:5px; font-weight:600;'>• Juan Efraín Pacheco S.</p>
        <p style='margin-bottom:0px; font-weight:600;'>• Sofía Hinojosa Rocha</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Marco Estratégico (NYZ Logy 2050)")
    st.markdown("""
    <div class='sidebar-box'>
        <h4>👁️ Misión</h4>
        <p style='font-size:13px; color:#475569;'>Entregar dispositivos de comunicación confiables con soluciones de IA y ciberseguridad que mejoren la conectividad y protejan los datos del cliente.</p>
    </div>
    <div class='sidebar-box'>
        <h4>🚀 Visión</h4>
        <p style='font-size:13px; color:#475569;'>Ser un líder global en hardware de telecomunicaciones a través de la innovación, conectividad segura y un sólido desempeño financiero.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# BANNER PRINCIPAL / PORTADA DEL DASHBOARD
# -------------------------------------------------------------
st.markdown("""
<div class='title-banner'>
    <h1>CUADRO DE MANDO INTEGRAL</h1>
    <p>Balanced Scorecard de Gobernanza Estratégica | NYZ Logy 2050 — Campus León</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# PANEL 1: PANEL PRINCIPAL CON TODOS LOS KPI (Vista Ejecutiva Global)
# -------------------------------------------------------------
st.markdown("<div class='section-header'>PANEL 1: Panel de Control Ejecutivo (Consolidado Global de KPIs)</div>", unsafe_allow_html=True)

st.write("Esta sección presenta la situación actual consolidada de los Indicadores Clave de Rendimiento (KPI) clave frente a las metas de largo plazo fijadas para la corporación. Los colores representan la perspectiva estratégica correspondiente.")

# Fila de Tarjetas Gigantes de KPIs Centrales (Un KPI representativo de cada perspectiva)
col_p1, col_p2, col_p3, col_p4 = st.columns(4)

with col_p1:
    st.markdown("""
    <div class='kpi-card fin-card'>
        <h3>Margen de Utilidad Neta</h3>
        <div class='value'>14.5%</div>
        <div class='meta'>Meta: 18.0% (Año 2028)</div>
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div class='kpi-card cli-card'>
        <h3>Net Promoter Score (NPS)</h3>
        <div class='value'>51 pts</div>
        <div class='meta'>Meta: 70 pts (Año 2027)</div>
    </div>
    """, unsafe_allow_html=True)

with col_p3:
    st.markdown("""
    <div class='kpi-card proc-card'>
        <h3>Costo Operativo / Unidad</h3>
        <div class='value'>-12.0%</div>
        <div class='meta'>Meta: -20.0% (Año 2027)</div>
    </div>
    """, unsafe_allow_html=True)

with col_p4:
    st.markdown("""
    <div class='kpi-card cap-card'>
        <h3>Ingenieros Certificados en IA</h3>
        <div class='value'>45.0%</div>
        <div class='meta'>Meta: 80.0% (Año 2027)</div>
    </div>
    """, unsafe_allow_html=True)

# Gráfico Infográfico Global de Logro de Metas
st.write("")
st.markdown("#### 🎯 Porcentaje de Avance General Hacia la Meta")

# Datos para el gráfico de barras horizontal de avance
kpis_labels = [
    'Margen de Utilidad Neta (Financiera)', 
    'Cuota de Mercado Regional (Financiera)', 
    'Satisfacción de Clientes NPS (Cliente)', 
    'Preferencia de Marca (Cliente)',
    'Eficiencia de Costos Unitarios (Procesos)',
    'Mitigación de Vulnerabilidades (Procesos)',
    'Capacitación y Certificación IA (Capacidad)',
    'Sprints de Innovación Lanzados (Capacidad)'
]
porcentajes_avance = [80.5, 65.0, 72.8, 69.1, 60.0, 85.0, 56.2, 75.0]
colores_grafico = ['#ef4444', '#ef4444', '#14b8a6', '#14b8a6', '#10b981', '#10b981', '#f59e0b', '#f59e0b']

fig_global = go.Figure(go.Bar(
    x=porcentajes_avance,
    y=kpis_labels,
    orientation='h',
    marker_color=colores_grafico,
    text=[f"{x}%" for x in porcentajes_avance],
    textposition='inside',
    textfont=dict(color='white', size=14)
))

fig_global.update_layout(
    xaxis=dict(title="Porcentaje de Cumplimiento de la Meta Final (%)", range=[0, 100], gridcolor='#cbd5e1'),
    yaxis=dict(autorange="reversed", font=dict(size=13)),
    margin=dict(l=20, r=20, t=10, b=30),
    height=400,
    plot_bgcolor='white',
    paper_bgcolor='rgba(0,0,0,0)'
)
st.plotly_chart(fig_global, use_container_width=True)


# -------------------------------------------------------------
# PANEL 2: PANEL DE CONTROL DIVIDIDO POR PERSPECTIVA CON SUS KPI
# -------------------------------------------------------------
st.markdown("<div class='section-header'>PANEL 2: Desglose Detallado por Perspectiva Estratégica</div>", unsafe_allow_html=True)
st.write("A continuación se desglosan de forma visual y abierta las cuatro dimensiones del Balanced Scorecard. Cada sección expone de manera explícita sus objetivos, indicadores de resultado (*Lagging*), proyectos estratégicos asignados e indicadores de ejecución (*Leading*).")

# --- PERSPECTIVA 1: FINANCIERA ---
st.markdown("<h3 style='color:#b91c1c; border-bottom: 2px solid #ef4444; padding-bottom:5px; margin-top:25px;'>🟥 1. Perspectiva Financiera (Crecimiento y Rentabilidad)</h3>", unsafe_allow_html=True)
c1_f, c2_f = st.columns([1, 1])

with c1_f:
    st.markdown("""
    **Objetivo Estratégico principal:** Incrementar la rentabilidad corporativa y expandir agresivamente la presencia de la marca en las economías globales Tier-1.
    
    * **KPI de Resultado (Lagging Indicator):** Margen de Utilidad Neta (Línea base original $\rightarrow$ Meta del **18%** para 2028).
    * **Iniciativa Estratégica (Proyecto):** Lanzamiento global del modelo de suscripción premium *HomeGuard Subscription Plan*.
    * **KPI de Ejecución (Leading Indicator):** Número de nuevas suscripciones pagadas capturadas por trimestre.
    """)

with c2_f:
    st.markdown("""
    * **KPI de Resultado Alterno:** Incremento de Ingresos por Cuota de Mercado (Meta de **+12%** de crecimiento acumulado en Alemania, Japón y Canadá para 2029).
    * **Iniciativa Estratégica (Proyecto):** *Project Global Nexus* (Expansión masiva de alianzas con cadenas minoristas internacionales).
    * **KPI de Ejecución (Leading Indicator):** Número de nuevos contratos de distribución firmados formalmente por trimestre.
    """)

# --- PERSPECTIVA 2: CLIENTE ---
st.markdown("<h3 style='color:#0d9488; border-bottom: 2px solid #14b8a6; padding-bottom:5px; margin-top:35px;'>🟩 2. Perspectiva del Cliente (Propuesta de Valor y Lealtad)</h3>", unsafe_allow_html=True)
c1_c, c2_c = st.columns([1, 1])

with c1_c:
    st.markdown("""
    **Objetivo Estratégico principal:** Construir relaciones basadas en la confianza absoluta, ciberseguridad avanzada y diferenciación tecnológica frente a competidores directos.
    
    * **KPI de Resultado (Lagging Indicator):** Net Promoter Score (NPS) global (Línea base crítica de 32 $\rightarrow$ Meta de **70 puntos** para 2027).
    * **Iniciativa Estratégica (Proyecto):** Campaña masiva de concientización para el consumidor *"Secure by Design"*.
    * **KPI de Ejecución (Leading Indicator):** Volumen total de clientes activos alcanzados e interactuando con la campaña.
    """)

with c2_c:
    st.markdown("""
    * **KPI de Resultado Alterno:** Índice de Preferencia de Marca de Hardware (Meta del **55%** de usuarios seleccionando a NYZ sobre la competencia para 2028).
    * **Iniciativa Estratégica (Proyecto):** Programa de desarrollo de funciones de valor añadido impulsadas por Inteligencia Artificial.
    * **KPI de Ejecución (Leading Indicator):** Cantidad de nuevas características con IA nativa integradas y liberadas al mercado por año.
    """)

# --- PERSPECTIVA 3: PROCESOS INTERNOS ---
st.markdown("<h3 style='color:#059669; border-bottom: 2px solid #10b981; padding-bottom:5px; margin-top:35px;'>🟦 3. Perspectiva de Procesos Internos (Excelencia Operativa y Seguridad)</h3>", unsafe_allow_html=True)
c1_p, c2_p = st.columns([1, 1])

with c1_p:
    st.markdown("""
    **Objetivo Estratégico principal:** Optimizar las cadenas de suministro internacionales y blindar por completo la infraestructura digital y de propiedad intelectual de la empresa.
    
    * **KPI de Resultado (Lagging Indicator):** Reducción drástica del Costo Operativo por Unidad Producida (Meta de **-20%** de ahorro total para el cierre de 2027).
    * **Iniciativa Estratégica (Proyecto):** *Project NeuroChain* (Modelos predictivos de optimización de rutas y almacenamiento entre plantas de Alemania y Canadá).
    * **KPI de Ejecución (Leading Indicator):** Porcentaje de unidades de inventario (SKUs) controladas de extremo a extremo por algoritmos inteligentes.
    """)

with c2_p:
    st.markdown("""
    * **KPI de Resultado Alterno:** Control riguroso de riesgos de TI (Meta estricta de mantener **menos de 3 vulnerabilidades críticas** expuestas por trimestre para 2027).
    * **Iniciativa Estratégica (Proyecto):** *Project Sentinel-X* (Despliegue de nodos de detección automática y autónoma de amenazas digitales).
    * **KPI de Ejecución (Leading Indicator):** Porcentaje total de los nodos críticos de la red corporativa bajo monitoreo automatizado con IA.
    """)

# --- PERSPECTIVA 4: CAPACIDAD ORGANIZACIONAL ---
st.markdown("<h3 style='color:#d97706; border-bottom: 2px solid #f59e0b; padding-bottom:5px; margin-top:35px;'>🟨 4. Perspectiva de Capacidad Organizacional (Capital Humano e Innovación)</h3>", unsafe_allow_html=True)
c1_o, c2_o = st.columns([1, 1])

with c1_o:
    st.markdown("""
    **Objetivo Estratégico principal:** Desarrollar al máximo las competencias tecnológicas internas del personal y fomentar un ecosistema ágil de innovación continua.
    
    * **KPI de Resultado (Lagging Indicator):** Porcentaje de Ingenieros con Certificación Avanzada en IA y Ciberseguridad (Línea base del 10% $\rightarrow$ Meta del **80%** para 2027).
    * **Iniciativa Estratégica (Proyecto):** *Project TalentForge AI* (Universidad interna corporativa para el desarrollo y Upskilling técnico).
    * **KPI de Ejecución (Leading Indicator):** Número acumulado de empleados que acreditan exitosamente sus módulos de certificación.
    """)

with c2_o:
    st.markdown("""
    * **KPI de Resultado Alterno:** Ritmo de Innovación del Portafolio (Línea base de 2 $\rightarrow$ Meta de **6 nuevas funciones/productos disruptivos** lanzados por año para 2027).
    * **Iniciativa Estratégica (Proyecto):** Establecimiento institucional de Sprints de Innovación Cruzada Interfuncional.
    * **KPI de Ejecución (Leading Indicator):** Número total de talleres de Sprints de innovación completados satisfactoriamente por trimestre.
    """)


# -------------------------------------------------------------
# MÓDULO DE VALOR INGENIERÍA FINANCIERA (De la Actividad 7)
# -------------------------------------------------------------
st.markdown("<div class='section-header'>🌟 SECCIÓN ESPECIAL: Evaluación Financiera de Iniciativas (Gobernanza del Capital)</div>", unsafe_allow_html=True)
st.write("Para asegurar el cumplimiento del criterio de rigor analítico y creatividad, esta sección integra las métricas formales de presupuesto de capital calculadas en la Actividad 7. Demuestra la viabilidad presupuestal de los proyectos fondeados bajo un costo de capital del 10%.")

# Tabla de Presupuesto de Capital formateada como Infografía Limpia
data_financiera = {
    "Iniciativa Estratégica": ["Project NeuroChain", "Project Sentinel-X", "Project TalentForge AI", "Project Global Nexus"],
    "Inversión Inicial": ["$450,000", "$380,000", "$220,000", "$520,000"],
    "Payback Period": ["2.1 Años", "2.4 Años", "2.8 Años", "1.9 Años"],
    "Valor Presente Neto (VPN)": ["$77,160", "$52,945", "$25,342", "$112,044"],
    "Tasa Interna Retorno (TIR)": ["19.6%", "17.8%", "16.7%", "22.5%"],
    "Índice de Rentabilidad (PI)": ["1.17", "1.14", "1.12", "1.22"],
    "Dictamen Ejecutivo": ["🟩 GO", "🟩 GO", "🟩 GO", "🟩 GO"]
}
df_fin = pd.DataFrame(data_financiera)

# Mostrar tabla nativa limpia, grande y bien espaciada
st.table(df_fin)

# Gráfico comparativo de VPN por Iniciativa
st.write("")
st.markdown("#### 💰 Comparativa de Generación de Valor Neto (VPN)")

proyectos_nombres = df_fin["Iniciativa Estratégica"].tolist()
vpns_valores = [77160, 52945, 25342, 112044]

fig_vpn = go.Figure(go.Bar(
    x=proyectos_nombres,
    y=vpns_valores,
    marker_color=['#1e3a8a', '#3b82f6', '#60a5fa', '#93c5fd'],
    text=[f"${x:,.0f}" for x in vpns_valores],
    textposition='auto',
    textfont=dict(size=14, color='white')
))

fig_vpn.update_layout(
    xaxis=dict(title="Proyectos Autorizados"),
    yaxis=dict(title="Valor Presente Neto en USD ($)", gridcolor='#e2e8f0'),
    plot_bgcolor='white',
    height=350,
    margin=dict(l=20, r=20, t=20, b=20)
)
st.plotly_chart(fig_vpn, use_container_width=True)

# Pie de página institucional
st.markdown("<hr style='margin:40px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 12px;'>NYZ Logy 2050 Dashboard • Desarrollado para la materia Strategic Thinking • Tecnológico de Monterrey Campus León, 2026.</p>", unsafe_allow_html=True)
