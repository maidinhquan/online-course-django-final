from pathlib import Path
root = Path(__file__).resolve().parents[1]
def test_files_exist():
    required=['onlinecourse/models.py','onlinecourse/admin.py','onlinecourse/views.py','onlinecourse/urls.py','onlinecourse/templates/onlinecourse/course_details_bootstrap.html','onlinecourse/templates/onlinecourse/exam_result_bootstrap.html']
    assert all((root/f).exists() for f in required)
