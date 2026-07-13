import streamlit as st
import yt_dlp
import os
import time

# ১. ওয়েবসাইটের থিম এবং লেআউট সেটআপ
st.set_page_config(page_title="Ultra HD Downloader Pro", page_icon="🎬", layout="centered")

# CSS দিয়ে ওয়েবসাইটটিকে প্রফেশনাল ও আকর্ষণীয় লুক দেওয়া
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background-color: #00ffcc;
        color: #000000;
        font-weight: bold;
        border-radius: 8px;
        padding: 14px 28px;
        border: none;
        width: 100%;
        font-size: 16px;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #00cc99;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ২. টপ ব্যানার বিজ্ঞাপন (ইউজারদের ইম্প্রেশনের মাধ্যমে ইনকাম বাড়াতে)
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
st.write("যেকোনো ভিডিও বা মুভির লিংক দিন এবং কিবোর্ডের Enter বা Go চাপুন।")

# ৩. লিংক ইনপুট নেওয়ার ঘর
url = st.text_input("এখানে ভিডিও বা মুভির লিংকটি পেস্ট করুন:", placeholder="https://...")

if url:
    st.info("🔄 সার্ভারে ফাইলটি দ্রুত প্রসেস হচ্ছে... অনুগ্রহ করে অপেক্ষা করুন।")
    
    output_mp4 = 'fast_download.mp4'
    if os.path.exists(output_mp4):
        os.remove(output_mp4)
        
    # কম এমবি, ফাস্ট ডাউনলোড এবং আইপি ব্লক বাইপাস করার কনফিগারেশন
    ydl_opts = {
        'format': 'best[ext=mp4]/best', 
        'outtmpl': output_mp4,
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        if os.path.exists(output_mp4):
            st.success("✅ ফাইল প্রসেসিং সম্পূর্ণ হয়েছে!")
            
            # ৪. টাইমার ও হাই-সিপিএম স্পনসরড বক্স
            st.markdown("### ⏳ আপনার উচ্চ-গতির ডাউনলোড লিংকটি তৈরি হচ্ছে...")
            ad_box = st.empty()
            
            # ৩০ সেকেন্ডের কাউন্টডাউন টাইমার
            for seconds in range(30, 0, -1):
                ad_box.markdown(
                    f"""
                    <div style="border: 2px solid #00ffcc; padding: 25px; text-align: center; border-radius: 8px; background-color: #0f0f12; color: white;">
                        <p style="color: #ff4b4b; font-weight: bold; margin: 0; font-size: 18px;">⏱️ লিংক রেডি হচ্ছে: {seconds} সেকেন্ড বাকি</p>
                        <p style="font-size: 14px; color: #ccfffa; margin-top: 10px; font-weight: bold;">💎 আর্নিং বোনাস সক্রিয় করতে নিচের ব্যানারে ক্লিক করতে পারেন।</p>
                        <div style="margin-top: 15px; padding: 10px; background: #222; border-radius: 4px; color: #aaa; font-size: 12px;">
                            [ হাই-সিপিএম ভিডিও স্পনসরড বিজ্ঞাপন লোড হচ্ছে ]
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(1)
            
            ad_box.empty()
            
            # ৫. আপনার আসল Adsterra স্মার্টলিংক এখানে যুক্ত করা হয়েছে
            adsterra_smartlink = "https://www.effectivecpmnetwork.com/ucta0hugm?key=a3570034e5eb3da9881e385e48bde033"
            
            # জাভাস্ক্রিপ্ট কোড: এই বাটনে চাপ দিলেই নতুন ট্যাবে আপনার Adsterra লিংক ওপেন হবে
            st.markdown(
                f"""
                <script>
                    var buttons = window.parent.document.querySelectorAll("button");
                    buttons.forEach(function(button) {{
                        if (button.innerText.includes("⬇️ ডাউনলোড করুন (ফাস্ট সার্ভার)")) {{
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
                    label="⬇️ ডাউনলোড করুন (ফাস্ট সার্ভার)",
                    data=file,
                    file_name="Premium_Video.mp4",
                    mime="video/mp4"
                )
            
            os.remove(output_mp4)
        else:
            st.error("ফাইলটি সার্ভারে খুঁজে পাওয়া যায়নি। অনুগ্রহ করে সঠিক লিংক দিন।")
            
    except Exception as e:
        st.error("ডাউনলোড প্রসেস করতে সমস্যা হয়েছে। সার্ভার আইপি সাময়িকভাবে ওভারলোডেড হতে পারে। অনুগ্রহ করে লিংকটি পুনরায় চেক করুন অথবা অন্য কোনো লিংক দিয়ে চেষ্টা করুন।")
