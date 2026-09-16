import java.util.Properties

plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

val klucz = Properties().apply {
    val f = rootProject.file("klucz.properties")
    if (f.exists()) f.inputStream().use { load(it) }
}

android {
    namespace = "pl.maslak.fizykaquiz"
    compileSdk = 34

    defaultConfig {
        applicationId = "pl.maslak.fizykaquiz"
        // minSdk 24 — telefon docelowy to Samsung M21 z Androidem 12 (API 31).
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }

    signingConfigs {
        create("wydanie") {
            if (klucz.getProperty("storeFile") != null) {
                storeFile = file(klucz.getProperty("storeFile"))
                storePassword = klucz.getProperty("storePassword")
                keyAlias = klucz.getProperty("keyAlias")
                keyPassword = klucz.getProperty("keyPassword")
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            signingConfig = if (klucz.getProperty("storeFile") != null)
                signingConfigs.getByName("wydanie") else signingConfigs.getByName("debug")
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.6.1")
}
