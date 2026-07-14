import streamlit as st
import requests

st.set_page_config(page_title="Ultra HD Downloader Pro", page_icon="🎬", layout="centered")

st.markdown(
    """
    <div style="background-color: #1e1e24; padding: 15px; text-align: center; border-radius: 8px; border: 1px solid #333; margin-bottom: 25px;">
        <p style="color: #00ffcc; margin: 0; font-size: 11px; font-weight: bold; letter-spacing: 1px;">HIGH PREMIUM SPONSOR</p>
        <h4 style="color: #ffffff; margin: 5px 0; font-size: 16px;">🔥 Premium High-Paying Ad Live Here</h4>
        <p style="color: #aaa; margin: 0; font-size: 12px;">(বিজ্ঞাপনে ক্লিক করে আমাদের সাপোর্ট করুন)</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.title("🎬 প্রফেশনাল ওয়ান-ক্লিক ফাস্ট ডাউনলোডার")
st.write("যেকোনো ভিডিওর লিংক দিন এবং কিবোর্ডের Enter চাপুন।")

url = st.text_input("এখানে ভিডিও বা মুভির লিংকটি পেস্ট করুন:", placeholder="https://...")

if url:
    st.info("🔄 হাই-স্পিড ক্লাউড এপিআই-এর সাথে সংযোগ করা হচ্ছে...")
    
    # ভিডিও প্রসেস করার জন্য Cobalt API ব্যবহার (যা ইউটিউব আইপি ব্লক সহজেই বাইপাস করে)
    api_url = "https://api.cobalt.tools/api/json"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "url": url,
        "videoQuality": "720", # ফাস্ট এবং কম এমবি ফাইলের জন্য অপ্টিমাইজড
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        result = response.json()
        
        if response.status_code == 200 and "url" in result:
            download_link = result["url"]
            st.success("✅ আপনার ফাইল প্রসেসিং সম্পন্ন হয়েছে!")
            
            # Adsterra স্মার্টলিংক
            adsterra_smartlink = "https://www.effectivecpmnetwork.com/ucta0hugm?key=a3570034e5eb3da9881e385e48bde033"
            
            # এই বাটনে চাপ দিলেই রিডাইরেক্ট হয়ে Adsterra এবং ডাউনলোড একই সাথে ঘটবে
            st.markdown(
                f"""
                <a href="{download_link}" target="_blank" onclick="window.open('{adsterra_smartlink}', '_blank');" style="text-decoration: none;">
                    <button style="background-color: #00ffcc; color: #000; font-weight: bold; border-radius: 8px; padding: 15px; width: 100%; border: none; font-size: 18px; cursor: pointer;">
                        ⬇️ ডাউনলোড করুন (সুপার-ফাস্ট সার্ভার)
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("ভিডিও ফাইলটি খুঁজে পাওয়া যায়নি বা এই লিংকটি এপিআই দ্বারা সমর্থিত নয়।")
    except Exception as e:
        st.error("সার্ভার ওভারলোডেড। অনুগ্রহ করে কিছুক্ষণ পর আবার চেষ্টা করুন।")
