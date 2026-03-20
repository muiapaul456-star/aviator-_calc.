import streamlit as st

st.set_page_config(page_title="Aviator Pro Calc", layout="centered")

st.title("🚀 Aviator Pro: Risk & Kelly Manager")
st.markdown("---")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    balance = st.number_value("Total Balance (KES/USD)", min_value=0.0, value=1000.0)
with col2:
    target_mult = st.number_input("Target Cash-Out (e.g. 2.0)", min_value=1.01, value=2.0)

# 1. Probability Math
p = 0.97 / target_mult  # Win Probability
q = 1 - p               # Loss Probability
b = target_mult - 1     # Net Odds

# 2. Kelly Criterion Formula
# f = (bp - q) / b
if b > 0:
    kelly_f = (b * p - q) / b
else:
    kelly_f = 0

# UI Output
st.subheader("📊 Mathematical Reality")
st.write(f"Chance of hitting {target_mult}x: **{p*100:.2f}%**")

st.divider()

st.subheader("💰 Smart Stake Recommendations")
full_kelly_stake = max(0, balance * kelly_f)
half_kelly_stake = full_kelly_stake / 2

c1, c2 = st.columns(2)
c1.metric("Full Kelly (Aggressive)", f"{full_kelly_stake:.2f}")
c2.metric("Half Kelly (Recommended)", f"{half_kelly_stake:.2f}")

st.info("💡 **Why use Half-Kelly?** It drastically reduces your 'Risk of Ruin' (going broke) while still growing your bankroll mathematically over time.")

st.warning("⚠️ This tool is for educational purposes. Aviator is a game of chance with a built-in house edge.")
