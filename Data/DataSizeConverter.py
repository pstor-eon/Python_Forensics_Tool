def data_calculator():
    units = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4}

    size = float(input("데이터 크기를 입력하세요.: "))
    input_unit = input("입력 단위를 입력하세요 (B, KB, MB, GB, TB): ").upper()
    output_unit = input("출력 단위를 입력하세요 (B, KB, MB, GB, TB): ").upper()

    if input_unit not in units or output_unit not in units:
        print("입력 또는 출력 단위가 잘못되었습니다. B, KB, MB, GB 또는 TB를 사용하십시오.")
        return

    input_bytes = size * units[input_unit]
    output_size = input_bytes / units[output_unit]

    print(f"{size:,.2f} {input_unit} 는 {output_size:,.2f} {output_unit} 와 같습니다.")

if __name__ == "__main__":
    data_calculator()
