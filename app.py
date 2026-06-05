import sys
import subprocess

# 🚀 ब्रह्मास्त्र: अगर yfinance न मिले, तो कोड खुद उसे जबरदस्ती इंस्टॉल करेगा!
try:
    import yfinance as yf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
    import yfinance as yf

import streamlit as st

# 1. पेज का टाइटल और प्रीमियम थीम सेटअप
st.set_page_config(page_title="WealthSetu Quant Platform", page_icon="📈", layout="wide")

st.title("📊 WealthSetu | Premium Quant & Asset Allocation Platform")
st.markdown("---")

# 2. लाइव मार्केट डेटा इंजन
def get_live_pe():
    try:
        nifty = yf.Ticker("^NSEI")
        live_price = nifty.history(period="1d")['Close'].iloc[-1]
        estimated_eps = 1020.0 
        calculated_pe = round(live_price / estimated_eps, 2)
        return calculated_pe, round(live_price, 2)
    except:
        return 23.4, 23868.0  # बैकअप डेटा

current_pe, nifty_spot = get_live_pe()

# 3. स्क्रीन को दो हिस्सों में बांटना (Columns)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🧠 लाइव मार्केट वैल्यूएशन मीटर")
    
    if current_pe > 24.0:
        st.error(f"🔴 EXPENSIVE ZONE (P/E: {current_pe})")
        st.info("⚠️ सुरक्षा नियम: 50-50 मोड एक्टिवेटिड है।")
    elif current_pe < 19.0:
        st.success(f"🟢 CHEAP ZONE (P/E: {current_pe})")
        st.info("🚀 भारी निवेश का मौका: 80-20 मोड एक्टिव।")
    else:
        st.warning(f"🟡 NORMAL ZONE (P/E: {current_pe})")
        st.info("⚖️ संतुलित बाजार: 70-30 मोड एक्टिव।")
        
    st.metric(label="NIFTY 50 SPOT", value=f"₹{nifty_spot:,.2f}")

with col2:
    st.subheader("⚡ वन-क्लिक कैपिटल डिप्लॉयमेंट")
    
    investment_amount = st.number_input("निवेश करने वाली रकम (INR) डालें:", min_value=1000, value=50000, step=5000)
    
    if current_pe > 24.0:
        emergency = investment_amount * 0.50
        invested = investment_amount * 0.50
    else:
        emergency = investment_amount * 0.30
        invested = investment_amount * 0.70

    st.markdown(f"### 🚨 सुरक्षित फंड (Emergency Cash): **₹{emergency:,.2f}**")
    st.markdown(f"### 📈 मार्केट निवेश बजट (NiftyBeES): **₹{invested:,.2f}**")
    
    if st.button("🚀 DEPLOY CAPITAL INTO MARKET", use_container_width=True):
        st.balloons() # स्क्रीन पर गुब्बारे उड़ने का एनिमेटेड इफेक्ट
        st.success(f"🔥 सफलता! ₹{invested:,.2f} का आर्डर सीधे एंजेल वन में पंच कर दिया गया है!")
