from django.db import models

# 이사업체 정보
class MovingCompany(models.Model):
    id = models.AutoField(primary_key=True) # Column ID
    name = models.CharField(null=False, max_length=256, default="") # 업체명
    ceo = models.CharField(null=False, max_length=256, default="") # 대표이사
    tel = models.CharField(null=False, unique=True, max_length=15, default="") # 연락처
    address = models.CharField(null=False, max_length=1024, unique=True, default="") # 주소정보
    business_number = models.CharField(null=False, max_length=256, unique=True, default="") # 사업자번호
    business_reg_date = models.DateTimeField(null=False) # 사업자등록일자
    number_of_employees = models.IntegerField(null=False) # 직원 수
    number_of_vehicles = models.IntegerField(null=False) # 차량 수(1톤, 2.5톤, 5톤)
    reservation_status = models.BooleanField(default=False) # 매칭가능여부

    class Meta:
        db_table = "moving_company"


# 가정이사 신청 접수 정보
class MovingReservation(models.Model):
    id = models.AutoField(primary_key=True) # Column ID
    name = models.CharField(null=False, max_length=256, default="") # 이름
    tel = models.CharField(null=False, max_length=15, default="") # 연락처
    start_address = models.CharField(null=False, max_length=256, default="") # 출발지 주소정보
    start_floor = models.IntegerField(null=False) # 출발지 층수
    end_address = models.CharField(null=False, max_length=256, default="") # 도착지 주소정보
    end_floor = models.IntegerField(null=False) # 도착지 층수
    moving_date = models.DateTimeField(null=False) # 이사 일자
    is_storage = models.BooleanField(null=False, default=False) # 보관이사여부
    agreement_information_collection = models.BooleanField(null=False) # 이용약관동의여부
    agreement_sharing_collected_information = models.BooleanField(null=False) # 견젹요청을 위한 개인정보 제3자 제공동의여부
    agreement_marketing = models.BooleanField(null=False) # 마케팅 정보수신 동의 여부

    class Meta:
        db_table = "moving_reservation"


# 고객정보
class CustomerInformation(models.Model):
    # 이름, 연락처, 등록일, 이용약관동의여부, 견적요청을 위한 개인정보 제3자 제공동의여부, 마케팅 정보수신 동의여부
    id = models.AutoField(primary_key=True) # Column ID
    name = models.CharField(null=False, max_length=256, default="") # 이름
    tel = models.CharField(null=False, max_length=15, default="") # 연락처
    reg_date = models.DateTimeField(null=False, auto_now_add=True)
    agreement_information_collection = models.BooleanField(null=False) # 이용약관동의여부
    agreement_sharing_collected_information = models.BooleanField(null=False) # 견젹요청을 위한 개인정보 제3자 제공동의여부
    agreement_marketing = models.BooleanField(null=False) # 마케팅 정보수신 동의 여부

    class Meta:
        db_table = "customer_information"


# 고객 피드백 이력
class CustomerFeedbackLog(models.Model):
    # 고객정보, 업체정보, 이사종류(가정이사, 원룸이사), 정보공개동의여부, 전문성 만족도(매우만족, 만족, 보통, 불만족, 매우불만족), 가격 만족도(매우만족, 만족, 보통, 불만족, 매우불만족), 친절 만족도(매우만족, 만족, 보통, 불만족, 매우불만족), 재방문의사, 계약가격, 이사일, 피드백 작성일, 피드백 내용
    id = models.AutoField(primary_key=True) # Column ID
    customer = models.ForeignKey(CustomerInformation, on_delete=models.SET_NULL, null=True) # 고객정보
    company = models.ForeignKey(MovingCompany, on_delete=models.SET_NULL, null=True) # 업체정보
    move_type = models.IntegerField(null=False) # 가정이사 : 0, 원룸이사 : 1
    agreement_open_information = models.BooleanField(null=False, default=False) # 정보공개동의여부
    satisfied_pro = models.IntegerField(null=False) # 전문성 만족도 - 매우불만족 : 1, 불만족 : 2, 보통 : 3, 만족 : 4, 매우만족 : 5
    satisfied_price = models.IntegerField(null=False) # 가격 만족도 - 매우불만족 : 1, 불만족 : 2, 보통 : 3, 만족 : 4, 매우만족 : 5
    satisfied_kindness = models.IntegerField(null=False) # 친절 만족도 - 매우불만족 : 1, 불만족 : 2, 보통 : 3, 만족 : 4, 매우만족 : 5
    revisit = models.BooleanField(null=False, default=False) # 재방문의사
    payment = models.IntegerField(null=False) # 계약가격
    moving_date = models.DateTimeField(null=False) # 이사일
    feedback_date = models.DateTimeField(null=False, auto_now_add=True) # 피드백 작성일
    feedback_text = models.TextField(null=False) # 피드백 내용

    class Meta:
        db_table = "customer_feedback_log"

