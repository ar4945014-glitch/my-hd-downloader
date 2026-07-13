import streamlit as st
import yt_dlp
import os
import time

# ১. ওয়েবসাইটের থিম এবং লেআউট সেটআপ
st.set_page_config(page_title="Ultra HD Downloader Pro", page_icon="🎬", layout="centered")

# ২. ব্যানার বিজ্ঞাপন (Adsterra বা ডেমো ব্যানার)
st.markdown(
    """
    <div style="background-color: #1e1e24; padding: 15px; text-align: center; border-radius: 8px; border: 1px solid #333; margin-bottom: 25px;">
        <p style="color: #00ffcc; margin: 0; font-size: 11px; font-weight: bold; letter-spacing: 1px;">HIGH PREMIUM SPONSOR</p>
        <h4 style="color: #ffffff; margin: 5px 0; font-size: 16px;">🔥 Premium High-Paying Banner Ad Live Here</h4>
        <p style="color: #aaa; margin: 0; font-size: 12px;">(এখানে আপনার ইউজারদের জন্য ইনকামের মূল ব্যানারটি দেখাবে)</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.title("🎬 প্রফেশনাল ওয়ান-ক্লিক এইচডি ডাউনলোডার")
st.write("যেকোনো মুভি বা ভিডিওর লিংক দিন এবং কিবোর্ডের Enter বা Go চাপুন।")

# ৩. লিংক ইনপুট নেওয়ার ঘর
url = st.text_input("এখানে ভিডিও বা মুভির লিংকটি পেস্ট করুন:", placeholder="https://...")

if url:
    st.info("🔄 সার্ভারে প্রসেস হচ্ছে... অনুগ্রহ করে অপেক্ষা করুন।")
    
    output_mp4 = 'downloaded_video.mp4'
    if os.path.exists(output_mp4):
        os.remove(output_mp4)
        
    # HTTP 403 Forbidden এবং ব্লকিং সমস্যা এড়ানোর জন্য উন্নত ব্রাউজার হেডার অপশন
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_mp4,
        'quiet': True,
        'no_warnings': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Mode': 'navigate',
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        if os.path.exists(output_mp4):
            st.success("✅ ফাইল প্রসেসিং সম্পূর্ণ হয়েছে!")
            
            # ৪. টাইমার ও বিজ্ঞাপন বক্স (৩০ সেকেন্ড কাউন্টডাউন)
            st.markdown("### ⏳ আপনার ডাউনলোড লিংকটি তৈরি হচ্ছে...")
            video_ad_box = st.empty()
            
            for seconds in range(30, 0, -1):
                video_ad_box.markdown(
                    f"""
                    <div style="border: 2px solid #00ffcc; padding: 20px; text-align: center; border-radius: 8px; background-color: #0f0f12; color: white;">
                        <p style="color: #ff4b4b; font-weight: bold; margin: 0; font-size: 16px;">⏱️ লিংক রেডি হচ্ছে: {seconds} সেকেন্ড বাকি</p>
                        <p style="font-size: 14px; color: #ccc; margin-top: 5px;">এখানে আপনার ইনকামের হাই-আর্নিং ভিডিও বিজ্ঞাপনটি চলবে।</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(1)
            
            video_ad_box.empty()
            
            # ৫. আপনার আসল Adsterra স্মার্টলিংক কোড (যা ক্লিক করলেই নতুন ট্যাবে অ্যাড খুলবে)
            adsterra_smartlink = "https://www.effectivecpmnetwork.com/ucta0hugm?key=a3570034e5eb3da9881e385e48bde033"
            
            st.markdown(
                f"""
                <script>
                    var buttons = window.parent.document.querySelectorAll("button");
                    buttons.forEach(function(button) {{
                        if (button.innerText.includes("আপনার ফোনে ফুল এইচডি মুভিটি ডাউনলোড করুন")) {{
                            button.addEventListener("click", function() {{
                                window.open("{adsterra_smartlink}", "_blank");
                            }});
                        }}
                    }});
                </script>
                """,
                unsafe_allow_html=True
            )
            
            # চূড়ান্ত ডাউনলোড বাটন
            with open(output_mp4, "rb") as file:
                st.download_button(
                    label="⬇️ আপনার ফোনে ফুল এইচডি মুভিটি ডাউনলোড করুন",
                    data=file,
                    file_name="Downloaded_Video.mp4",
                    mime="video/mp4"
                )
            
            os.remove(output_mp4)
        else:
            st.error("ফাইলটি পাওয়া যায়নি। অনুগ্রহ করে সঠিক লিংক দিয়ে আবার চেষ্টা করুন।")
            
    except Exception as e:
        st.error("ডাউনলোড প্রসেস করতে সমস্যা হয়েছে। সার্ভার বা আইপি সাময়িকভাবে ব্লক থাকতে পারে। দয়া করে অন্য কোনো ভিডিওর লিংক দিয়ে চেষ্টা করুন।")
