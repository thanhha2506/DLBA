import streamlit as st

def display_results(result):
    """
    Hiển thị kết quả trả về từ backend lên giao diện Streamlit.
    """
    if not result or "result" not in result:
        st.error("No result received from backend.")
        return

    res = result["result"]

    st.markdown("### 🧩 **Detected Result**")
    st.markdown(f"**Fruit Type:** {res.get('fruit_type', 'Unknown').capitalize()}")
    st.markdown(f"**Confidence:** {res.get('confidence', 0)*100:.2f}%")
    st.markdown(f"**Defect Status:** {res.get('defect_status', '-')}")
    st.markdown(f"**Ripeness:** {res.get('ripeness_status', '-')}")
    st.markdown(f"**Final State:** {res.get('final_state', '-')}")
    st.markdown(f"**Final Score:** {res.get('final_score', 0):.2f}")

    # Hiển thị thông báo theo tình trạng
    if res.get("final_state") == "harvestable":
        st.success("✅ Trái cây đạt chuẩn thu hoạch!")
    elif res.get("final_state") == "not_harvestable":
        st.warning("🟡 Trái cây chưa đạt chuẩn, cần thời gian chín thêm.")
    else:
        st.info("ℹ️ Không thể xác định rõ trạng thái trái cây.")
