#!/usr/bin/env ruby
if ARGV.length == 2
  if ARGV[1] == "ipaddress"
    begin
      file = File.open(ARGV[0], 'r')
      file_contents = file.read
      ipaddresses = file_contents.scan(/(?<ipaddresses>^\d\S+)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts ipaddresses
        end
      elsif response == "view"
        puts ipaddresses
      else
        puts ipaddresses
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      # ensures file closing
      file.close if file
    end
  elsif ARGV[1] == "timestamp"
    begin
      file = File.open(ARGV[0], 'r')
      file_contents = file.read
      timestamps = file_contents.scan(/(?<timestamp>.{26})(?<=\d)]/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts timestamps
        end
      elsif response == "view"
        puts timestamps
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  elsif ARGV[1] == "httpmethod"
    begin
      file = File.open(ARGV[0], 'r')
      file_contents = file.read
      httpmethods = file_contents.scan(/"(?=\w)(?<httpmethod>\w+.*\w)"/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts httpmethods
        end
      elsif response == "view"
        puts httpmethods
      else
        puts httpmethods
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  elsif ARGV[1] == "statuscode"
    begin
      file = File.open(ARGV[0], 'r')
      file_contents = file.read
      statuscodes = file_contents.scan(/(?<=".)(?<statuscode>\d+)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts statuscodes
        end
      elsif response == "view"
        puts statuscodes
      else
        puts statuscodes
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  elsif ARGV[1] == "responsesize"
    begin
      file = File.open(ARGV[0], 'r')
      file_contents = file.read
      response_sizes = file_contents.scan(/(?<response-size>\d+$)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts response_sizes
        end
      elsif response == "view"
        puts response_sizes
      else
        puts response_sizes
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
  else
    puts "Log Data #{ARGV[1]} doesn't exist!!!"
  end
else
  # Enter the file name with its extension
  puts "Enter file name: "
  file_name = gets.chomp
  puts "Which type of information would you like to extract?"
  puts "ipaddress\ntimestamp\nhttpmethod\nstatuscode\nresponsesize"
  puts "Enter one of the options above: "
  log_data = gets.chomp
  if log_data == "ipaddress"
    begin
      file = File.open(file_name, 'r')
      file_contents = file.read
      ipaddresses = file_contents.scan(/(?<ipaddresses>^\d\S+)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts ipaddresses
        end
      elsif response == "view"
        puts ipaddresses
      else
        puts ipaddresses
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  elsif log_data == "timestamp"
    begin
      file = File.open(file_name, 'r')
      file_contents = file.read
      timestamps = file_contents.scan(/(?<timestamp>.{26})(?<=\d)]/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts timestamps
        end
      elsif response == "view"
        puts timestamps
      else
        puts timestamps
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  elsif log_data == "httpmethod"
    begin
      file = File.open(file_name, 'r')
      file_contents = file.read
      httpmethods = file_contents.scan(/"(?=\w)(?<httpmethod>\w+.*\w)"/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts httpmethods
        end
      elsif response == "view"
        puts httpmethods
      else
        puts httpmethods
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if close
    end
  elsif log_data == "statuscode"
    begin
      file = File.open(file_name, 'r')
      file_contents = file.read
      statuscodes = file_contents.scan(/(?<=".)(?<statuscode>\d+)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts statuscodes
        end
      elsif response == "view"
        puts statuscodes
      else
        puts statuscodes
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if close
    end
  elsif log_data == "responsesize"
    begin
      file = File.open(file_name, 'r')
      file_contents = file.read
      response_sizes = file_contents.scan(/(?<response-size>\d+$)/)
      puts "Do you want to view or save? "
      response = gets.chomp
      if response == "save"
        puts "Enter a file name: "
        filename = gets.chomp
        File.open(filename, 'w') do |file|
          file.puts response_sizes
        end
      elsif response == "view"
        puts response_sizes
      else
        puts response_sizes
      end
    rescue Errno::ENOENT => e
      # Handle case where file does not exist
      puts "An error occured: #{e}"
    rescue Errno::EACCES => e
      # Handle case where file doesn't have permission
      puts "An error occurred: #{e}"
    rescue => e
      # Handles other exceptions that may occur
      puts "An error occurred: #{e}"
    ensure
      file.close if file
    end
  else
    puts "Log Data #{log_data} doesn't exist!!!"
  end
end
