# congnghe - tech: 0, 
# suckhoe - health: 1, 
# thethao - sport: 2, 
# xe - car & motor: 3

from tensorflow.python.keras import models
import pickle

vectorizer = pickle.load(open("./model/vectorizer.pickle", "rb"))

text = """
 'Trâu cày' tiền ảo bị cân bán như sắt vụn ở Trung Quốc
Hàng nghìn thiết bị được bán tháo với giá rẻ hoặc xử lý tái chế như những sản phẩm điện tử phế liệu.

Những ngày qua, giá tiền ảo Bitcoin đã sụt mạnh, có lúc thấp hơn mốc 4.000 USD một đồng, khiến cộng đồng những người tham gia cuộc chơi tiền ảo điêu đứng.
 Theo ZOL, tại Trung Quốc, nơi chiếm tới 70% lượng tiền ảo được đào trên toàn cầu, rất nhiều nhà đầu tư phải bán tháo máy móc và thiết bị với mong muốn rút chân khỏi "vũng lầy" càng nhanh càng tốt. Một số người thậm chí đối xử với các cỗ máy đào tiền ảo từng có giá nghìn USD như rác thải, phế liệu.

Trước đây, những thiết bị này có giá hơn 20.000 nhân dân tệ (gần 3.000 USD) một chiếc. Nay chúng được chào mời với giá chỉ 1.500 nhân dân tệ (khoảng 200 USD), thậm chí thấp hơn, mà cũng không có người mua.
 Chia sẻ trên mạng xã hội Weibo và các diễn đàn tiền ảo, nhiều chủ mỏ đăng ảnh thu gom dọn dẹp "trâu cày" của mình, xếp chúng thành từng đống để chờ người tới xử lý.

Nhiều chủ mỏ đã coi chúng như phế liệu, tháo rời ra để giữ lại những linh kiện dùng được, còn lại đem cân bán như sắt vụn, nhằm thu hồi chút tiền vốn hoặc trang trải phần nào các chi phí hoặc khoản nợ.
"""


x_val = vectorizer.transform([text])

new_model = models.load_model('./model/MyModel.h5')

a = new_model.predict(x_val)

print(a[0])
