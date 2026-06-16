import streamlit as st
import base64

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)
photo_data = [
    {"image":"assets/photo1.jpg","text":"..."},
    {"image":"assets/photo2.jpg","text":"..."},
    {"image":"assets/photo3.jpg","text":"..."},
    {"image":"assets/photo4.jpg","text":"..."},
]
def gallery_page(data, idx_key, done_key, title):

    idx = st.session_state[idx_key]

    item = data[idx]

    st.title(title)

    col1,col2 = st.columns([3,2])

    with col1:
        st.image(item["image"], use_container_width=True)

    with col2:
        st.markdown(
            f"""
            <div class="chatbox">
                {item["text"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    if idx < len(data)-1:

        if st.button("➡️ Tiếp"):
            st.session_state[idx_key] += 1
            st.rerun()

    else:

        if st.button("💖 Quay lại Menu"):

            st.session_state[done_key] = True
            st.session_state[idx_key] = 0

            st.session_state.page = 100
            st.rerun()
food_data = [...]
trip_data = [...]
flower_data = [...]
# ==========================
# SESSION
# ==========================

if "page" not in st.session_state:
    st.session_state.page = 0
if "photo_done" not in st.session_state:
    st.session_state.photo_done = False

if "food_done" not in st.session_state:
    st.session_state.food_done = False

if "trip_done" not in st.session_state:
    st.session_state.trip_done = False

if "flower_done" not in st.session_state:
    st.session_state.flower_done = False
if "photo_idx" not in st.session_state:
    st.session_state.photo_idx = 0

if "food_idx" not in st.session_state:
    st.session_state.food_idx = 0

if "trip_idx" not in st.session_state:
    st.session_state.trip_idx = 0

if "flower_idx" not in st.session_state:
    st.session_state.flower_idx = 0
# ==========================
# DATA
# ==========================

stories = [
    {
        "image": "assets/me1.png",
        "audio": "assets/audio1.mp3",
        "text": "Helu bibi là anh đây Nguyễn Bá Việt Huy. Trước tiên thì anh cảm ơn em vì đã vô trang web này, đây là trang web anh làm cho riêng u and me, HÚ. Anh không có đủ thời gian để làm một web xịn hơn nhìu, có thể sẽ tốt hơn trong tương lai đóoo nhể bibi. Anh mong em sẽ coi hếc những tâm tư cuối cùng (nhưng mà sẽ hok phải cuối đâu nhể bibi) của anh và sẽ giúp em vui lên nhìu hơn! "
    },
    {
        "image": "assets/me3.png",
        "audio": "assets/audio3.mp3",
        "text": "Anh đã làm nhìu điều sai với em, anh đã không tôn trọng em nghĩ chỉ cãi nhau thôi là xong mà lại không tính đến cảm xúc của em ngày càng hao tụt hơn và dẫn đến như này. Anh quả là stupid, anh đã biết nó nghiêm trọng thế nào và mong được cho em thấy một anh tốt hơn."
    },
    {
        "image": "assets/me5.png",
        "audio": "assets/audio5.mp3",
        "text": "Bibi hãy coi với tâm trạng hết sức thoải mái và vui vẻ nha dù không giúp em về lại như trước nhma chắc chắn sẽ đáng thời gian của em đó."
    }
]

# ==========================
# IMAGE
# ==========================

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
def img64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #ffd6e7 0%,
        #ffe8c8 50%,
        #fff0f8 100%
    );
}

/* CHAT BOX */

.chatbox{

    width:80%;

    margin:auto;

    background:#1f1f1f;

    color:white;

    padding:25px;

    border-radius:25px;

    font-size:24px;

    text-align:center;

    box-shadow:0 8px 25px rgba(0,0,0,.25);

    animation:popup .8s ease;
}

.chatbox:after{

    content:"";

    display:block;

    margin:auto;

    margin-top:20px;

    width:0;
    height:0;

    border-left:18px solid transparent;
    border-right:18px solid transparent;
    border-top:22px solid #1f1f1f;
}

/* CHARACTER */

.character{

    text-align:center;

    margin-top:15px;
}

.character img{

    width:340px;

    filter:
        drop-shadow(
            0px 15px 20px rgba(0,0,0,.25)
        );

    animation:wobble 2s infinite ease-in-out;
}

/* POPUP */

@keyframes popup{

    from{
        opacity:0;
        transform:translateY(40px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* WOBBLE */

@keyframes wobble{

    0%{
        transform:rotate(-3deg);
    }

    25%{
        transform:rotate(2deg);
    }

    50%{
        transform:rotate(4deg);
    }

    75%{
        transform:rotate(-2deg);
    }

    100%{
        transform:rotate(-3deg);
    }
}

/* START PAGE */

.start-title{

    text-align:center;

    margin-top:120px;

    color:#333;
}

.start-title h1{
    font-size:70px;
}

.start-title h2{
    font-size:34px;
}

/* BUTTON */

div.stButton > button{

    width:100%;

    height:60px;

    border-radius:18px;

    font-size:22px;

    font-weight:bold;
}
/* RAIN */

.rain-wrapper{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    overflow:hidden;
    pointer-events:none;
}

.rain-photo{

    position:absolute;

    width:140px;

    border-radius:18px;

    border:8px solid white;

    box-shadow:0 10px 25px rgba(0,0,0,.25);

    animation:fall linear infinite;
}

@keyframes fall{

    0%{
        transform:
            translateY(-250px)
            rotate(-20deg);
    }

    100%{
        transform:
            translateY(120vh)
            rotate(20deg);
    }
}
.menu-card{

    background:white;

    border-radius:25px;

    padding:25px;

    text-align:center;

    box-shadow:0 10px 25px rgba(0,0,0,.15);

    margin-bottom:15px;
}

.menu-card h1{

    font-size:60px;

    margin-bottom:0;
}

.menu-card h2{

    color:#333;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# START PAGE
# ==========================

if st.session_state.page == 0:

    st.markdown("""
    <div class="start-title">
        <h1>❤️</h1>
        <h2>Có một điều muốn gửi tới em</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    if st.button("💖 BẮT ĐẦU"):
        st.session_state.page = 1
        st.rerun()

# ==========================
# STORY
# ==========================

elif 1 <= st.session_state.page <= len(stories):

    idx = st.session_state.page - 1

    story = stories[idx]

    img64 = image_to_base64(story["image"])

    st.markdown(
        f"""
        <div class="chatbox">
            {story["text"]}
        </div>

        <div class="character">
            <img src="data:image/png;base64,{img64}">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.audio(story["audio"])

    st.write("")

    if idx < len(stories) - 1:

        if st.button("➡️ Tiếp"):
            st.session_state.page += 1
            st.rerun()

    else:

        if st.button("❤️ Tiếp tục"):
            st.session_state.page = 50
            st.rerun()

# ==========================
# END
# ==========================

# ==========================
# PHOTO RAIN
# ==========================

elif st.session_state.page == 50:

    st.balloons()

    st.markdown("""
    <div style="
        text-align:center;
        margin-top:150px;
        font-size:42px;
        font-weight:bold;
        color:#444;
    ">
        🌸 Những ký ức đang hiện về... 🌸
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/rain1.jpg", width=180)
        st.image("assets/rain4.jpg", width=180)

    with col2:
        st.image("assets/rain2.jpg", width=180)
        st.image("assets/rain5.jpg", width=180)

    with col3:
        st.image("assets/rain3.jpg", width=180)
        st.image("assets/rain6.jpg", width=180)

    st.write("")
    st.write("")

    if st.button("✨ Tiếp tục ✨"):
        st.session_state.page = 100
        st.rerun()
# ==========================
# MENU
# ==========================

# ==========================
# MENU
# ==========================

elif st.session_state.page == 100:

    st.markdown("""
    <div class="start-title">
        <h1>💖</h1>
        <h2>Chọn một mục nha bibi</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ======================
    # LEFT
    # ======================

    with col1:

        st.markdown("""
        <div class="menu-card">
            <h1>📸</h1>
            <h2>Photobooth</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📸 Mở Photobooth"):
            st.session_state.page = 201
            st.rerun()

        if st.session_state.photo_done:
            st.success("✅ Đã xem")

        st.markdown("""
        <div class="menu-card">
            <h1>🍜</h1>
            <h2>Ăn uống</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🍜 Mở Ăn uống"):
            st.session_state.page = 301
            st.rerun()

        if st.session_state.food_done:
            st.success("✅ Đã xem")

    # ======================
    # RIGHT
    # ======================

    with col2:

        st.markdown("""
        <div class="menu-card">
            <h1>🚗</h1>
            <h2>Đi chơi</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚗 Mở Đi chơi"):
            st.session_state.page = 401
            st.rerun()

        if st.session_state.trip_done:
            st.success("✅ Đã xem")

        st.markdown("""
        <div class="menu-card">
            <h1>🌷</h1>
            <h2>Hoa</h2>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🌷 Mở Hoa"):
            st.session_state.page = 501
            st.rerun()

        if st.session_state.flower_done:
            st.success("✅ Đã xem")

    # ======================
    # SPECIAL UNLOCK
    # ======================

    if (
        st.session_state.photo_done and
        st.session_state.food_done and
        st.session_state.trip_done and
        st.session_state.flower_done
    ):

        st.markdown("---")

        st.success("✨ MỤC SPECIAL ĐÃ ĐƯỢC MỞ KHÓA ✨")

        if st.button("❤️ MỞ MỤC SPECIAL❤️"):
            st.session_state.page = 900
            st.rerun()
# ==========================
# PHOTOBOOTH
# ==========================

elif st.session_state.page == 201:

    st.title("📸 Photobooth")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/photo1.jpg")
        st.image("assets/photo2.jpg")

    with col2:
        st.image("assets/photo3.jpg")
        st.image("assets/photo4.jpg")

    if st.button("⬅️ Quay lại Menu"):

        st.session_state.photo_done = True
        st.session_state.page = 100
        st.rerun()


# ==========================
# FOOD
# ==========================

elif st.session_state.page == 301:

    st.title("🍜 Ăn uống")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/food1.jpg")
        st.image("assets/food2.jpg")
        

    with col2:
        st.image("assets/food4.jpg")
        st.image("assets/food5.jpg")
        st.image("assets/food3.jpg")

    if st.button("⬅️ Quay lại Menu"):

        st.session_state.food_done = True
        st.session_state.page = 100
        st.rerun()


# ==========================
# TRIP
# ==========================

elif st.session_state.page == 401:

    st.title("🚗 Đi chơi")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/trip1.jpg")
        st.image("assets/trip2.jpg")
        

    with col2:
        st.image("assets/trip4.jpg")
        st.image("assets/trip5.jpg")
        st.image("assets/trip3.jpg")

    if st.button("⬅️ Quay lại Menu"):

        st.session_state.trip_done = True
        st.session_state.page = 100
        st.rerun()


# ==========================
# FLOWER
# ==========================

elif st.session_state.page == 501:

    st.title("🌷 Hoa")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/flower1.jpg")
        st.image("assets/flower2.jpg")

    with col2:
        st.image("assets/flower4.jpg")
        st.image("assets/flower3.jpg")

    if st.button("⬅️ Quay lại Menu"):

        st.session_state.flower_done = True
        st.session_state.page = 100
        st.rerun()
elif st.session_state.page == 900:

    st.video("assets/special.mov")

    st.write("")

    if st.button("❤️ Xem lời cuối ❤️"):
        st.session_state.page = 999
        st.rerun()
# ==========================
# ENDING
# ==========================

elif st.session_state.page == 999:

    st.markdown("""
    <div class="start-title">
        <h1>❤️</h1>
        <h2>Lời cuối cùng</h2>
    </div>
    """, unsafe_allow_html=True)

    st.audio("assets/final.mp3")

    st.markdown("""
    <div class="chatbox">
        [Viết lời kết của bạn ở đây]

        Cảm ơn em đã dành thời gian xem hết những điều anh muốn gửi.
        Dù tương lai thế nào thì anh vẫn luôn trân trọng những kỷ niệm của chúng ta. ❤️
    </div>
    """, unsafe_allow_html=True)