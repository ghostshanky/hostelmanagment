import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="StayFinder - Find Your Community. Find Your Home.",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap');
body { font-family: 'Plus Jakarta Sans', sans-serif; }
.primary { color: #2b9dee; }
.background-light { background-color: #f6f7f8; }
.background-dark { background-color: #101a22; }
.orange-accent { color: #FFA500; }
.hero-bg {
    background-image: linear-gradient(rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0.5) 100%), url('https://lh3.googleusercontent.com/aida-public/AB6AXuBT9ls834uSRBR6QcNga1tnsjJUI6lNVrObMuhyG9Etwl-O559TpoWZxFYWU9pz_BCRxAxfIssOFk6_CRuHJ6vIAcJebgkGLmqSv7qwXc5UiJ7mvE0c-Za8c0X-TeifdaEJNUjQl-2otWoOCQpqFswA2tJYgWryrpl__NCX36YT60bsqfRTjI6eWwcmDawhrBfiK3VfLekfyYXtGMh3Kv_4EiZ6gx5-q5thDBBShXVYQEORIn5eKHmFsNsgM0pRTwRswMMcurO3a-Q');
    background-size: cover;
    background-position: center;
    border-radius: 0.75rem;
}
.card-bg-1 { background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCU1Drh0rqdaWUHOGHsHiICFNbnQ0H-NW87EoE509p4WlCwhzCza6V8w2-eZdwgtmMOs8WFkwyXexpW2W2FLiQrYP_Hj3sc7MPe_kBFXQO9ld93fHFMe10GhDCmKc2C5adjSIlptWQmhqBsRmFL49gh81JsHhmJUhmxV5-CH-hUdca1QnVE-tZ1OY_qC10ltuMqxTIvsrgjy5CPNW-rWTPMYJsyf_Y_tcZFdOJA670eVebLgbWNqXMN4w-oUSRBbx76oME7uzHZN4U'); }
.card-bg-2 { background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuC13YHX1O7VrmIU0suwYrYDLyNdFU-AwhzuI9dsDtO4Ni94PNefqgRTS7c-9SOPquiOIpp7stJSrsn08xMpKcYKz0wRSDFJI8-8NF2bAH85-y2MDp3ZbRupw-NSltq0731GNIhCdH2QW5eC-4NZQ1q7YgTWhXJJPba2JIMVPEt9XCXljIpOXHrfkORyrIKR0pqttFy9d42_jWkuzE8DHne47Uv_-fsB7xHcanLu7YgXsGq5IfzERgs9RMgoT_803jvEzWd01dP6UV4'); }
.card-bg-3 { background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuDh4v9rXBs1WetudUp9GahAHSn1jr_6b7phMl_qXmQZ-TSOLJ-pXvI2B_tiX_pfxSs4UoNjS_mpLt5i-MQ9VBokS2pJyuw_ShMPUxg03cHNmjD1hZhWqiYs7Hm58i-ej6n4vop4fIjkxocxAoWRntqx9muuaKLJFseq7uU317pYv9ADr-Y6vrTfgo2VFyAXpu-Y5meA8uEDgdboc-ZEqb0YSmQmn9t9ZarQYQox89zJgg8NJtA2GkdADp1kozqusdXdBYUu-VrQTZ8'); }
.card-bg-4 { background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCgHfvAXaotxry85YE0IVAGIlKjOxpVmG5iauywfxW0tsrZS0hElfZU54KnwV5zXs5T2kdObQvx0GzzDWW_gIS3lSBf1J-H4Vt6qCRZE-G9_hYf1EV_qwum-Ui7VHw6ola0JK3yYIiwZeixCJ-nOhRdV0TDymYskqxqqp3qJY93T2T8sA5706drjDSDPy4TtGwsgQDUwC8z8Y-yfmhlXihluzFD807WGKRwDId-vwPCUjdAFZSi5ZaHZKFYqmVk2LrpG7BDRMciZCY'); }
.testimonial-bg { background-color: #f6f7f8; }
.cta-bg { background-color: rgba(43, 157, 238, 0.1); }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Header
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; border-bottom: 1px solid #e5e7eb;">
    <div style="display: flex; align-items: center; gap: 0.5rem;">
        <div style="width: 1.5rem; height: 1.5rem; background-color: #2b9dee; border-radius: 50%;"></div>
        <h2 style="font-weight: bold; color: #2b9dee;">StayFinder</h2>
    </div>
    <div style="display: flex; gap: 2rem; align-items: center;">
        <a href="#" style="color: #374151; text-decoration: none;">List a Property</a>
        <a href="#" style="color: #374151; text-decoration: none;">Help</a>
        <button style="background-color: #2b9dee; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem;">Sign Up</button>
        <button style="background-color: #f3f4f6; color: #111518; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem;">Log In</button>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-bg" style="min-height: 480px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 2rem; border-radius: 0.75rem;">
    <div>
        <h1 style="color: white; font-size: 3rem; font-weight: 800;">Find Your Community. Find Your Home.</h1>
        <p style="color: white; font-size: 1rem; margin: 1rem 0;">Budget-friendly hostels and PGs for students and professionals. Book your perfect stay today.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Search Bar
col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
with col1:
    search = st.text_input("Search", placeholder="Enter a city or area", label_visibility="collapsed")
with col2:
    st.button("Stay Type")
with col3:
    st.button("Price Range")
with col4:
    st.button("Search", type="primary")

# Featured Listings
st.markdown("<h2 style='text-align: center; margin: 2rem 0;'>Explore Our Top-Rated Properties</h2>", unsafe_allow_html=True)
cols = st.columns(4)
listings = [
    {"name": "Urban Nest Hostel", "rating": 4.8, "location": "Downtown, Delhi", "price": "₹8,000/month", "bg": "card-bg-1"},
    {"name": "Pro Co-Living PG", "rating": 4.9, "location": "Koramangala, Bangalore", "price": "₹15,000/month", "bg": "card-bg-2"},
    {"name": "City Central Stays", "rating": 4.7, "location": "Bandra, Mumbai", "price": "₹12,000/month", "bg": "card-bg-3"},
    {"name": "The Student Hub", "rating": 4.8, "location": "Hinjewadi, Pune", "price": "₹9,500/month", "bg": "card-bg-4"},
]
for i, listing in enumerate(listings):
    with cols[i]:
        st.markdown(f"""
        <div style="background-size: cover; background-position: center; aspect-ratio: 4/3; border-radius: 0.5rem; margin-bottom: 1rem;" class="{listing['bg']}"></div>
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <p style="font-weight: bold;">{listing['name']}</p>
                <div style="display: flex; align-items: center; gap: 0.25rem;">
                    <span style="color: #FFA500;">★</span>
                    <span>{listing['rating']}</span>
                </div>
            </div>
            <p style="color: #6b7280; font-size: 0.875rem;">{listing['location']}</p>
            <p style="font-weight: 600;">{listing['price']}</p>
        </div>
        """, unsafe_allow_html=True)

# Value Proposition
st.markdown("""
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; text-align: center; padding: 2rem 0;">
    <div>
        <div style="width: 3rem; height: 3rem; background-color: rgba(43, 157, 238, 0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
            <span style="font-size: 1.5rem;">✓</span>
        </div>
        <h3 style="font-weight: bold;">Verified Stays</h3>
        <p style="color: #6b7280;">Every property is manually verified by our team to ensure quality and safety.</p>
    </div>
    <div>
        <div style="width: 3rem; height: 3rem; background-color: rgba(43, 157, 238, 0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
            <span style="font-size: 1.5rem;">💳</span>
        </div>
        <h3 style="font-weight: bold;">Secure Payments</h3>
        <p style="color: #6b7280;">Your booking and payment history, all in one place.</p>
    </div>
    <div>
        <div style="width: 3rem; height: 3rem; background-color: rgba(43, 157, 238, 0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
            <span style="font-size: 1.5rem;">👥</span>
        </div>
        <h3 style="font-weight: bold;">Vibrant Community</h3>
        <p style="color: #6b7280;">Connect with like-minded students and professionals.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials
st.markdown("""
<div class="testimonial-bg" style="padding: 3rem; border-radius: 0.75rem; margin: 2rem 0;">
    <h2 style="text-align: center; font-weight: bold; margin-bottom: 2rem;">Hear from our Community</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem;">
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuB71zZ2niCwr1eHdZ-9U4g1NXVWYwBN-ius2-nsjy18mrwwDRCU7nUfzoEGSzj8NcNfBhFZ86lvxoCA9XdtSeV3YW_Z4dAsuoWODueLIt8rZXQgta4lymu0mVPH7eBEZviQ-vZ8939xBC6rIFfMR76PZhzCHYgqv5Uvkn3zq3XJn6ryTZYZ_YoeNSh30vCbSxRaTmvHhQ_YEYRH-TXiutaufuXG5PwlUygZuxrC055rjhPa1-gOjDBiJDJnbVJhwFvshv-eq2HKedc" style="width: 3rem; height: 3rem; border-radius: 50%;">
                <div>
                    <p style="font-weight: bold;">Rohan Sharma</p>
                    <p style="color: #6b7280; font-size: 0.875rem;">Software Engineer</p>
                </div>
            </div>
            <p style="margin-bottom: 1rem;">"Finding a good PG in Bangalore was a nightmare until I found StayFinder. The process was so simple and the property was exactly as advertised."</p>
            <div style="color: #FFA500;">★★★★★</div>
        </div>
        <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAk0ry2qPtRRG3cgRCm7lWBThAeSO0OR5DKt1O6PcWTq09yC6wfceh8zsvhis0MMcJaZ1bHSPAh8MiMpp_j_0PvYyPRNa_9UK4xH8N1oM6NiPLSMhQqTgJeEVv3ovRqHbrOahoO2JsIfZheSMd_U-3bVYzf9BOAju8UWLoFEoorhFtHNEFGGUGsjWDMmj3lRTYiPpJSqAVt3xuTTdzQTuON75yg8XtzBZEj6o-GTFZNYiafAqazpuBQL8NCxFMyKGVu8bAa35lggJE" style="width: 3rem; height: 3rem; border-radius: 50%;">
                <div>
                    <p style="font-weight: bold;">Priya Mehta</p>
                    <p style="color: #6b7280; font-size: 0.875rem;">University Student</p>
                </div>
            </div>
            <p style="margin-bottom: 1rem;">"As a student, safety was my top priority. StayFinder's verified listings gave me peace of mind."</p>
            <div style="color: #FFA500;">★★★★☆</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-bg" style="padding: 3rem; border-radius: 0.75rem; text-align: center; margin: 2rem 0;">
    <h2 style="font-weight: bold; font-size: 1.5rem;">Earn by Listing Your Property</h2>
    <p style="color: #6b7280; margin: 1rem 0;">Join our community of hosts and turn your extra space into a reliable income stream.</p>
    <button style="background-color: #FFA500; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: bold;">Get Started</button>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="border-top: 1px solid #e5e7eb; padding: 2rem 0; margin-top: 2rem;">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 2rem;">
        <div>
            <h4 style="font-weight: bold; margin-bottom: 1rem;">StayFinder</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="#" style="color: #6b7280; text-decoration: none;">About Us</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Careers</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Press</a></li>
            </ul>
        </div>
        <div>
            <h4 style="font-weight: bold; margin-bottom: 1rem;">Discover</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Trust & Safety</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Travel Credit</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Community Events</a></li>
            </ul>
        </div>
        <div>
            <h4 style="font-weight: bold; margin-bottom: 1rem;">Hosting</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="#" style="color: #6b7280; text-decoration: none;">List your property</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Host Responsibly</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Community Center</a></li>
            </ul>
        </div>
        <div>
            <h4 style="font-weight: bold; margin-bottom: 1rem;">Support</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Help Center</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Contact Us</a></li>
                <li><a href="#" style="color: #6b7280; text-decoration: none;">Cancellation options</a></li>
            </ul>
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #e5e7eb; padding-top: 1rem;">
        <p style="color: #6b7280;">© 2024 StayFinder, Inc. All rights reserved.</p>
        <div style="display: flex; gap: 1rem;">
            <a href="#" style="color: #6b7280; text-decoration: none;">Privacy</a>
            <a href="#" style="color: #6b7280; text-decoration: none;">Terms</a>
            <a href="#" style="color: #6b7280; text-decoration: none;">Sitemap</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
