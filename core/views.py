from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.utils.timezone import localtime
from .models import Quiz, Question, Option, Attempt, Answer, Category
import csv
from io import TextIOWrapper


# ---------------- Public Views ----------------
=======

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Category
from .models import Quiz, Question, Option, Attempt, Answer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import csv
from io import TextIOWrapper
from django.db.models import Count


>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce

def home(request):
    categories = Category.objects.all()
    return render(request, 'core/home.html', {'categories': categories})


<<<<<<< HEAD
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
=======

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']
        confirm  = request.POST['confirm_password']
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce

        # Validate form
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

<<<<<<< HEAD
        # Create user safely
        User.objects.create_user(username=username, email=email, password=password)
=======
        # Save user with hashed password
        User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'core/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


<<<<<<< HEAD
def category_quizzes(request, category_id):
    quizzes = Quiz.objects.filter(category_id=category_id).annotate(total_questions=Count('question'))
    return render(request, 'core/quizzes_by_category.html', {'quizzes': quizzes})


=======

def category_quizzes(request, category_id):
    quizzes = Quiz.objects.filter(category_id=category_id)
    return render(request, 'core/quizzes_by_category.html', {'quizzes': quizzes})




>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if quiz.status != 'active':
        messages.warning(request, "This quiz is not currently active.")
<<<<<<< HEAD
        return redirect('quizzes_by_category', category_id=quiz.category.id)

    # Initialize session for quiz attempt
    request.session['quiz_id'] = quiz.id
    request.session['question_index'] = 0
    request.session['score'] = 0
    request.session['answers'] = {}

    return redirect('attempt_quiz')
=======
        return redirect('quizzes_by_category')

    questions = Question.objects.filter(quiz=quiz).order_by('?')
    return render(request, 'core/quiz_attempt.html', {
        'quiz': quiz,
        'questions': questions,
        'total_questions': questions.count()
    })






>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce


@login_required
def attempt_quiz(request):
    quiz_id = request.session.get('quiz_id')
    question_index = request.session.get('question_index', 0)
    quiz = get_object_or_404(Quiz, pk=quiz_id)
<<<<<<< HEAD
    questions = quiz.question_set.order_by('id')
=======
    questions = quiz.question_set.all()
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce

    if question_index >= len(questions):
        return redirect('quiz_result')

    current_question = questions[question_index]
    options = current_question.options.all()

    if request.method == 'POST':
        selected_option_id = request.POST.get('option')
        if selected_option_id:
<<<<<<< HEAD
            selected_option = get_object_or_404(Option, id=selected_option_id)

            # Update answers safely
            answers = request.session.get('answers', {})
            answers[str(current_question.id)] = selected_option.id
            request.session['answers'] = answers

=======
            selected_option = Option.objects.get(id=selected_option_id)
            # Store user's answer
            request.session['answers'][str(current_question.id)] = selected_option.id
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
            # Update score
            if selected_option.is_correct:
                request.session['score'] += 1

        # Move to next question
<<<<<<< HEAD
        request.session['question_index'] = question_index + 1
=======
        request.session['question_index'] += 1
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        return redirect('attempt_quiz')

    return render(request, 'core/quiz_attempt.html', {
        'question': current_question,
        'options': options,
        'question_number': question_index + 1,
        'total_questions': len(questions),
    })


<<<<<<< HEAD
=======

>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@login_required
def quiz_result(request):
    score = request.session.get('score', 0)
    quiz_id = request.session.get('quiz_id')
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    total_questions = quiz.question_set.count()
    answers = request.session.get('answers', {})

    # Save attempt
    attempt = Attempt.objects.create(
        user=request.user,
        quiz=quiz,
        score=score,
        total=total_questions,
    )

<<<<<<< HEAD
    # Save answers
    for qid, oid in answers.items():
        question = Question.objects.get(pk=qid)
        option = Option.objects.get(pk=oid)
        Answer.objects.create(attempt=attempt, question=question, selected_option=option)
=======
    # Save each answer
    for qid, oid in answers.items():
        question = Question.objects.get(pk=qid)
        option = Option.objects.get(pk=oid)
        Answer.objects.create(
            attempt=attempt,
            question=question,
            selected_option=option
        )
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce

    # Clear session
    for key in ['score', 'quiz_id', 'question_index', 'answers']:
        request.session.pop(key, None)

    return render(request, 'core/quiz_result.html', {
        'score': score,
        'total_questions': total_questions,
        'quiz': quiz
    })


@login_required
def my_attempts(request):
    attempts = Attempt.objects.filter(user=request.user).order_by('-completed_at')
<<<<<<< HEAD
    for attempt in attempts:
        attempt.completed_at = localtime(attempt.completed_at)
    return render(request, 'core/my_attempts.html', {'attempts': attempts})


# ---------------- Admin Views ----------------

@staff_member_required
def admin_dashboard(request):
=======
    return render(request, 'core/my_attempts.html', {'attempts': attempts})



@staff_member_required
def admin_dashboard(request):
    from .models import Quiz, Attempt
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
    context = {
        'total_users': User.objects.count(),
        'total_quizzes': Quiz.objects.count(),
        'total_attempts': Attempt.objects.count(),
        'top_quizzes': Quiz.objects.annotate(attempts=Count('attempt')).order_by('-attempts')[:5],
    }
    return render(request, 'core/admin_dashboard.html', context)


<<<<<<< HEAD
=======



>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_manage_users(request):
    users = User.objects.all()
    return render(request, 'core/admin_users.html', {'users': users})

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "User created successfully.")
        return redirect('admin_manage_users')
    return render(request, 'core/admin_add_user.html')

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        password = request.POST.get('password')
        if password:
            user.set_password(password)
<<<<<<< HEAD
            user.save()
            update_session_auth_hash(request, user)  # Prevents logout if editing own account
        else:
            user.save()
=======
        user.save()
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        messages.success(request, "User updated successfully.")
        return redirect('admin_manage_users')
    return render(request, 'core/admin_edit_user.html', {'user': user})

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted.")
    return redirect('admin_manage_users')

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def upload_users_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        file_data = TextIOWrapper(csv_file.file, encoding='utf-8')
        reader = csv.DictReader(file_data)
        for row in reader:
<<<<<<< HEAD
            try:
                username = row['username']
                email = row['email']
                password = row['password']
            except KeyError as e:
                messages.error(request, f"CSV missing column: {e}")
                continue

            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)

=======
            username = row['username']
            email = row['email']
            password = row['password']
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        messages.success(request, "Users uploaded successfully.")
        return redirect('admin_manage_users')
    return render(request, 'core/admin_upload_users.html')


<<<<<<< HEAD
=======

>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_manage_quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'core/admin_quizzes.html', {'quizzes': quizzes})

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_add_quiz(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        status = request.POST.get('status')

        category = get_object_or_404(Category, id=category_id)
        Quiz.objects.create(title=title, category=category, status=status)
        messages.success(request, "Quiz added successfully.")
        return redirect('admin_manage_quizzes')
    return render(request, 'core/admin_add_quiz.html', {'categories': categories})

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        quiz.title = request.POST.get('title')
        category_id = request.POST.get('category')
        quiz.category = get_object_or_404(Category, id=category_id)
        quiz.status = request.POST.get('status')
        quiz.save()
        messages.success(request, "Quiz updated successfully.")
        return redirect('admin_manage_quizzes')
    return render(request, 'core/admin_edit_quiz.html', {'quiz': quiz, 'categories': categories})

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def admin_delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    messages.success(request, "Quiz deleted.")
    return redirect('admin_manage_quizzes')

<<<<<<< HEAD

=======
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
@staff_member_required
def upload_quizzes_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        file_data = TextIOWrapper(csv_file.file, encoding='utf-8')
        reader = csv.DictReader(file_data)
        for row in reader:
<<<<<<< HEAD
            try:
                category_name = row['category']
                title = row['title']
                status = row.get('status', 'active')
            except KeyError as e:
                messages.error(request, f"CSV missing column: {e}")
                continue

            category, _ = Category.objects.get_or_create(name=category_name)
            Quiz.objects.create(title=title, category=category, status=status)

=======
            category_name = row['category']
            category, _ = Category.objects.get_or_create(name=category_name)
            Quiz.objects.create(
                title=row['title'],
                category=category,
                status=row.get('status', 'active')
            )
>>>>>>> 019875c9addcb4c44f022ed3c1f97382028c9bce
        messages.success(request, "Quizzes uploaded successfully.")
        return redirect('admin_manage_quizzes')
    return render(request, 'core/admin_upload_quizzes.html')
