-- =========================================
-- PONCTIA
-- Gestion intelligente des retards étudiants
-- =========================================

CREATE DATABASE IF NOT EXISTS ponctia
    CHARACTER SET utf8mb4;

USE ponctia;


-- =========================================
-- TABLE : CLASSES
-- =========================================

CREATE TABLE IF NOT EXISTS classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- =========================================
-- TABLE : UTILISATEURS
-- =========================================

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(191) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    role ENUM('student', 'teacher', 'admin')
        NOT NULL DEFAULT 'student',

    class_id INT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY unique_user_email (email),

    CONSTRAINT fk_user_class
        FOREIGN KEY (class_id)
        REFERENCES classes(id)
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- =========================================
-- TABLE : PROFESSEURS
-- =========================================

CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(191) NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY unique_teacher_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- =========================================
-- TABLE : COURS
-- =========================================

CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    teacher_id INT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_course_teacher
        FOREIGN KEY (teacher_id)
        REFERENCES teachers(id)
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- =========================================
-- TABLE : RETARDS
-- =========================================

CREATE TABLE IF NOT EXISTS latenesses (
    id INT AUTO_INCREMENT PRIMARY KEY,

    student_id INT NOT NULL,
    course_id INT NULL,

    lateness_date DATE NOT NULL,
    arrival_time TIME NOT NULL,
    duration_minutes INT NOT NULL,

    reason VARCHAR(255) NOT NULL,
    comment TEXT NULL,

    status ENUM('pending', 'justified', 'rejected')
        NOT NULL DEFAULT 'pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_lateness_student
        FOREIGN KEY (student_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_lateness_course
        FOREIGN KEY (course_id)
        REFERENCES courses(id)
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;