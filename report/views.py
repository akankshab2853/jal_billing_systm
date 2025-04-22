from django.http import HttpResponse
import openpyxl
from datetime import datetime

def generate_excel_report(request):
    # Get date range from request
    start_date_str = request.GET.get("start_date")
    end_date_str = request.GET.get("end_date")

    # Validate inputs
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except Exception:
        return HttpResponse("Invalid date format. Use YYYY-MM-DD.", status=400)

    # Create a blank workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Blank Report"

    # You can optionally include the date range in the header or sheet
    ws.append([f"Report from {start_date} to {end_date}"])

    # Prepare response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    filename = f"blank_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    # Save workbook to response
    wb.save(response)

    return response
