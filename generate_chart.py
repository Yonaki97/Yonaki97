import matplotlib.pyplot as plt
import sys
import io
import base64

def generate_chart():
    # Data untuk pie chart
    labels = ["Total semua materi", "Banyak user", "Total semua quiz", 
              "Total semua course", "Total materi VIDEO", "Total semua PPT", "Total semua PDF"]
    values = [38, 37, 20, 18, 15, 13, 10]
    colors = ["#3498db", "#9b59b6", "#1abc9c", "#2ecc71", "#f1c40f", "#e67e22", "#e74c3c"]

    # Membuat pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    # Simpan gambar sebagai base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return img_base64

if __name__ == "__main__":
    # Print base64 string ke stdout agar dapat diambil oleh Node.js
    print(generate_chart())
