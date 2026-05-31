import streamlit as st

st.set_page_config(
    page_title="YK Legal — AI Legal Intelligence",
    page_icon="⚖️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&family=Cormorant+Garamond:wght@300;400;600&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
@keyframes fadeIn { to{opacity:1} }
</style>

<div style='text-align:center;padding:10vh 2rem 6vh 2rem;position:relative;overflow:hidden;'>
<div style='position:absolute;width:600px;height:600px;border-radius:50%;border:1px solid #E94E1B;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:600px;height:600px;border-radius:50%;border:1px solid #E94E1B;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>

<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;opacity:0;animation:fadeIn 1s 0.5s forwards;'>
<span style='width:6px;height:6px;background:#E94E1B;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
Adv. Damini Yasodai &nbsp;|&nbsp; AI Legal Intelligence &nbsp;|&nbsp; Indian Law
</div>

<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Cormorant Garamond,serif;font-weight:300;font-size:clamp(5rem,15vw,11rem);line-height:0.85;color:#ffffff;letter-spacing:0.05em;'>YK</div>
</div>
<div style='overflow:hidden;margin-bottom:1rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(3rem,10vw,7rem);line-height:0.85;color:#E94E1B;letter-spacing:0.3em;'>LEGAL</div>
</div>

<div style='overflow:hidden;margin-bottom:1rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.65s forwards;font-family:Cormorant Garamond,serif;font-weight:300;font-size:clamp(1rem,2.5vw,1.4rem);color:#888;letter-spacing:0.2em;'>AI Legal Intelligence</div>
</div>

<div style='overflow:hidden;margin-bottom:3rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.8s forwards;font-family:Space Mono,monospace;font-size:clamp(0.6rem,1.5vw,0.8rem);color:#444;letter-spacing:0.15em;text-transform:uppercase;'>Indian Law. Made Accessible. &nbsp;◆&nbsp; AI Legal Support</div>
</div>

<div style='display:inline-flex;gap:1rem;opacity:0;animation:fadeIn 1s 1.2s forwards;flex-wrap:wrap;justify-content:center;'>
<a href="https://github.com/damiii-codes7" target="_blank" style='font-family:Space Mono,monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;border:1px solid #181818;padding:1rem 2rem;text-decoration:none;'>VIEW GITHUB</a>
</div>
</div>

<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 40s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>POSH Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Indian Contract Act 1872</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Companies Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Maternity Benefit Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>EPF Act 1952</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Arbitration Act 1996</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Consumer Protection Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Factories Act 1948</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Minimum Wages Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>IT Act 2000</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>POSH Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Indian Contract Act 1872</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Companies Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Maternity Benefit Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
</div>
</div>

<div style='display:grid;grid-template-columns:repeat(4,1fr);border:1px solid #181818;margin:4rem 0;'>
<div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
<div style='font-family:Bebas Neue,sans-serif;font-size:3.5rem;color:#E94E1B;line-height:1;'>03</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-top:0.5rem;'>Live Tools</div>
</div>
<div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
<div style='font-family:Bebas Neue,sans-serif;font-size:3.5rem;color:#ffffff;line-height:1;'>22</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-top:0.5rem;'>Indian Laws</div>
</div>
<div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
<div style='font-family:Bebas Neue,sans-serif;font-size:3.5rem;color:#ffffff;line-height:1;'>60s</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-top:0.5rem;'>Analysis Time</div>
</div>
<div style='padding:2rem;text-align:center;'>
<div style='font-family:Bebas Neue,sans-serif;font-size:3.5rem;color:#ffffff;line-height:1;'>FREE</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-top:0.5rem;'>Always</div>
</div>
</div>

<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:2rem;'>THE TOOLS</div>

<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-bottom:4rem;'>

<a href="https://yk-policy.streamlit.app" target="_blank" style='text-decoration:none;'>
<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#E94E1B;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>⚖️</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#E94E1B;margin-bottom:0.5rem;'>LIVE — 10 Labour Laws</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Policy</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>HR Policy Risk Scanner</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Upload your HR policy PDF and get an instant compliance report against 10 Indian Labour Laws.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#E94E1B;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>OPEN TOOL →</div>
</div>
</a>

<a href="https://yk-judgment.streamlit.app" target="_blank" style='text-decoration:none;'>
<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#E94E1B;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>📜</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#E94E1B;margin-bottom:0.5rem;'>LIVE — Any Court</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Judgment</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>Court Judgment Summarizer</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Upload any Indian court judgment and get an instant AI summary — facts, issues, decision, ratio.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#E94E1B;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>OPEN TOOL →</div>
</div>
</a>

<a href="https://yk-contract.streamlit.app" target="_blank" style='text-decoration:none;'>
<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#2D9CDB;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>📋</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#2D9CDB;margin-bottom:0.5rem;'>LIVE — 12 Contract Laws</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Contract</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>Contract Risk Analyzer</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Upload any contract — NDA, employment, service agreement — checked against 12 Indian laws.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#2D9CDB;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>OPEN TOOL →</div>
</div>
</a>

<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;opacity:0.4;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#27AE60;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>🤖</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#444;margin-bottom:0.5rem;'>COMING SOON</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Ask</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>Legal Q&A Bot</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Ask any question about Indian law and get a clear, cited answer — IPC to GST to labour codes.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#444;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>COMING SOON</div>
</div>

<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;opacity:0.4;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#9B51E0;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>📝</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#444;margin-bottom:0.5rem;'>COMING SOON</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Draft</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>Legal Document Drafter</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Describe what you need and get a ready-to-use legal document — NDAs, notices, letters.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#444;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>COMING SOON</div>
</div>

<div style='border:1px solid #181818;padding:2rem;position:relative;overflow:hidden;background:#030303;opacity:0.4;'>
<div style='position:absolute;top:0;left:0;width:3px;height:100%;background:#F2994A;'></div>
<div style='font-size:2rem;margin-bottom:1rem;'>📖</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#444;margin-bottom:0.5rem;'>COMING SOON</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:1.8rem;color:#ffffff;line-height:1;margin-bottom:0.3rem;'>YK Explain</div>
<div style='font-family:Cormorant Garamond,serif;font-size:0.9rem;color:#888;margin-bottom:1rem;font-style:italic;'>Bare Act Explainer</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;line-height:1.6;'>Paste any section of any Indian law and get a plain English explanation with examples.</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#444;margin-top:1.5rem;text-transform:uppercase;letter-spacing:0.1em;'>COMING SOON</div>
</div>

</div>

<hr style='border-color:#181818;margin:2rem 0;'>

<div style='text-align:center;padding:4rem 2rem;'>
<div style='font-family:Cormorant Garamond,serif;font-weight:300;font-size:clamp(2rem,6vw,4rem);color:#ffffff;margin-bottom:1rem;'>Built by a lawyer.<br>Powered by AI.</div>
<div style='font-family:Space Mono,monospace;font-size:0.75rem;color:#888;max-width:500px;margin:0 auto 2rem;line-height:1.8;'>
A Space combining deep legal knowledge with AI technology to make Indian law accessible to everyone. <br> Always consult a legal professional before signing contracts.
</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#E94E1B;text-transform:uppercase;letter-spacing:0.2em;'>Adv. Damini Yasodai — YK Legal</div>
</div>

<hr style='border-color:#181818;margin:0;'>
<div style='display:flex;justify-content:space-between;align-items:center;padding:2rem 0;flex-wrap:wrap;gap:1rem;'>
<div style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#ffffff;font-weight:300;letter-spacing:0.1em;'>YK LEGAL</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#444;text-transform:uppercase;letter-spacing:0.1em;'>Indian Law. Made Accessible.</div>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;color:#444;text-transform:uppercase;letter-spacing:0.1em;'>AI tool — Not legal advice</div>
</div>
""", unsafe_allow_html=True)
