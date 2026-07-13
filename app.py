import streamlit as st
import yt_dlp
import os
import subprocess
import time

# ১. ওয়েবসাইটের থিম এবং লেআউট সেটআপ (ভবিষ্যতে আপডেট করার জন্য রেডি করা)
st.set_page_config(page_title="Ultra HD Downloader Pro", page_icon="🎬", layout="centered")

# ২. [💰 ব্যানার বিজ্ঞাপন - অপশন ১] 
# (এখানে কোনো খারাপ/অ্যাডাল্ট অ্যাড আসবে না। হাই-আর্নিং সেফ ব্যানার অ্যাড সেট করা হয়েছে)
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
st.write("যেকোনো মুভি বা ভিডিওর লিংক দিন। কম এমবি-তে ফুল এইচডি কোয়ালিটিতে দ্রুত ডাউনলোড হবে।")

# ৩. লিংক ইনপুট নেওয়ার ঘর
url = st.text_input("এখানে ভিডিও বা মুভির লিংকটি পেস্ট করুন:", placeholder="https://...")

# ৪. ডাউনলোডের মূল লজিক (যা কোনো লোডিং ছাড়াই সুপার-ফাস্ট কাজ করবে)
if url:
    st.info("🔄 সার্ভারে প্রসেস হচ্ছে... অনুগ্রহ করে অপেক্ষা করুন।")
    
    output_template = 'downloaded_video.%(ext)s'
    output_mp4 = 'downloaded_video.mp4'
    compressed_mp4 = 'final_hd_low_mb.mp4'
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'quiet': True, # অতিরিক্ত লোডিং কমাবে
    }
    
    try:
        # ক্লাউড সার্ভারে হাই-স্পিড ডাউনলোড
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        if os.path.exists(output_mp4):
            # গ্রাফিক্স ঠিক রেখে কম এমবি করার ইঞ্জিন (H.265 Technology)
            ffmpeg_cmd = f'ffmpeg -i {output_mp4} -vcodec libx265 -crf 23 -preset fast -acodec copy {compressed_mp4} -y'
            subprocess.run(ffmpeg_cmd, shell=True)
            
            if os.path.exists(compressed_mp4):
                st.success("✅ ফাইল প্রসেসিং সম্পূর্ণ হয়েছে!")
                
                # ৫. [💰 ভিডিও বিজ্ঞাপন / টাইমার - অপশন ২]
                # ডাউনলোড বাটনের ঠিক আগে ৩০ সেকেন্ডের সেফ কাউন্টডাউন অ্যাড
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
                
                # টাইমার শেষ হলে বিজ্ঞাপনের বক্স চলে যাবে এবং ডাউনলোড বাটন আসবে
                video_ad_box.empty()
                
                # -------------------------------------------------------------
                # 💰 Adsterra স্মার্টলিংক কোড (বাটনে ক্লিক করলেই অ্যাড ওপেন হবে)
                # -------------------------------------------------------------
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
                with open(compressed_mp4, "rb") as file:
                    st.download_button(
                        label="⬇️ আপনার ফোনে ফুল এইচডি মুভিটি ডাউনলোড করুন",
                        data=file,
                        file_name="Full_HD_Movie.mp4",
                        mime="video/mp4"
                    )
                
                # সার্ভার পরিষ্কার করা (পারফরমেন্স ফাস্ট রাখার জন্য)
                os.remove(output_mp4)
                os.remove(compressed_mp4)
            else:
                st.error("কোয়ালিটি প্রসেস করতে কিছুটা সমস্যা হয়েছে।")
        else:
            st.error("ফাইলটি পাওয়া যায়নি। সঠিক লিংক দিন।")
            
    except Exception as e:
        st.error(f"একটি সমস্যা হয়েছে: {str(e)}")

# ৬. ⚙️ ভবিষ্যতে নতুন ফিচার (যেমন: ভিডিও প্লেয়ার) যুক্ত করার জন্য খালি স্পেস
# (এটি ওয়েবসাইটে এখন দেখা যাবে না, কিন্তু পরে আপডেট করতে সাহায্য করবে)
def future_updates():
    pass

