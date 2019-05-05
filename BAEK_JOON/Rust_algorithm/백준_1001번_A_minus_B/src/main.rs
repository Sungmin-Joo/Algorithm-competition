use std::io;
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s)
		.expect("x");
    let a = &s[..1].to_string();
    let b = &s[2..3].to_string();
    let a: i32 = a.parse()
        .expect("x");
    let b: i32 = b.parse()
        .expect("x");
    println!("{}",a - b);
}
