import logging
import os
import time
import warnings
import logging.handlers # Explicitly import the handlers module

# --- Global Cleanup Function ---
# Function to remove existing log files for a clean run
def clean_log_files(*filenames):
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up: {filename}")

# --- 1. Basic Logging Configuration ---
# By default, logging outputs to the console (stderr) with a level of WARNING.
# You can change the basic configuration to set the level and format.

# Reset any previous basicConfig to avoid duplicate handlers if script is run multiple times
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("This is an informational message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.debug("This is a debug message. (Won't be shown with INFO level)")

# --- 2. Logging to a File ---
# You can direct log messages to a file instead of or in addition to the console.

log_file_name = "my_application.log"
clean_log_files(log_file_name)

# Create a logger instance
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG) # Set the lowest level for this logger
file_logger.propagate = False # Prevent messages from being passed to the root logger

# Create a file handler
file_handler = logging.FileHandler(log_file_name)
file_handler.setLevel(logging.DEBUG) # Set the lowest level for the handler

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
file_logger.addHandler(file_handler)

file_logger.debug("This is a debug message logged to file.")
file_logger.info("This is an info message logged to file.")
file_logger.warning("This is a warning message logged to file.")
file_logger.error("This is an error message logged to file.")
file_logger.critical("This is a critical message logged to file.")

# --- 3. Logging to Both Console and File ---
# You can have multiple handlers for a single logger.

# Create another logger instance
dual_logger = logging.getLogger("dual_logger")
dual_logger.setLevel(logging.DEBUG)
dual_logger.propagate = False # Prevent messages from being passed to the root logger

# Clear existing handlers for dual_logger if any (important for re-runs)
for handler in dual_logger.handlers[:]:
    dual_logger.removeHandler(handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Only INFO and above for console
console_handler.setFormatter(formatter) # Reuse the formatter

# File handler (different file for clarity)
dual_log_file_name = "dual_output.log"
clean_log_files(dual_log_file_name)

dual_file_handler = logging.FileHandler(dual_log_file_name)
dual_file_handler.setLevel(logging.DEBUG) # All levels for file
dual_file_handler.setFormatter(formatter)

# Add both handlers to the dual logger
dual_logger.addHandler(console_handler)
dual_logger.addHandler(dual_file_handler)

dual_logger.debug("This debug message goes only to dual_output.log")
dual_logger.info("This info message goes to console and dual_output.log")
dual_logger.error("This error message goes to console and dual_output.log")

# --- 4. Exception Logging ---
# Logging exceptions is crucial for debugging.

try:
    result = 10 / 0
except ZeroDivisionError: # Catching specific error is good practice
    logging.error("An error occurred during division:", exc_info=True)
    # exc_info=True will add exception information to the log message,
    # including the traceback.

# Using logging.exception() - a convenience function
try:
    int("not_a_number")
except ValueError:
    logging.exception("Failed to convert string to integer.")
    # logging.exception() is equivalent to logging.error(exc_info=True)
    # and is only called from an exception handler.

# --- 5. Best Practices / Common Use Cases ---

# It's common to get a logger for each module/file using __name__
# This helps in identifying the source of log messages.
module_logger = logging.getLogger(__name__)
module_logger.setLevel(logging.INFO)
# If you want this logger to also output to console/file, you need to add handlers
# or ensure that the root logger (configured with basicConfig) is handling it.
# For simplicity, if basicConfig is already set up, this logger will inherit handlers.

module_logger.info("Message from a specific module (using __name__).")

# Example of a function using logging
def calculate_something(a, b):
    module_logger.debug(f"Calculating with a={a}, b={b}")
    if b == 0:
        module_logger.error("Attempted division by zero!")
        return None
    return a / b

result = calculate_something(20, 5)
if result is not None:
    module_logger.info(f"Calculation result: {result}")

calculate_something(15, 0)

# --- 6. Advanced Scenarios: Log Rotation (RotatingFileHandler) ---
# Useful for preventing log files from growing indefinitely.
# Rotates logs when a certain size is reached, keeping a specified number of backups.

rotating_log_file = "rotating_app.log"
clean_log_files(rotating_log_file, rotating_log_file + ".1", rotating_log_file + ".2") # Clean up potential old rotated files

rotating_logger = logging.getLogger("rotating_logger")
rotating_logger.setLevel(logging.DEBUG)
rotating_logger.propagate = False

# Max 1KB per file, keep 3 backup files
rotating_handler = logging.handlers.RotatingFileHandler(
    rotating_log_file,
    maxBytes=1024, # 1 KB
    backupCount=3
)
rotating_handler.setFormatter(formatter)
rotating_logger.addHandler(rotating_handler)

print("\n--- Testing RotatingFileHandler (check rotating_app.log and its backups) ---")
for i in range(200): # Write enough messages to trigger rotation
    rotating_logger.info(f"Rotating log message {i:03d} - " + "A" * 50) # Add some length to messages
    time.sleep(0.01) # Small delay to ensure distinct timestamps

# --- 7. Advanced Scenarios: Timed Log Rotation (TimedRotatingFileHandler) ---
# Rotates logs based on time intervals (e.g., daily, hourly).

timed_rotating_log_file = "timed_rotating_app.log"
clean_log_files(timed_rotating_log_file) # Clean up the main file

timed_rotating_logger = logging.getLogger("timed_rotating_logger")
timed_rotating_logger.setLevel(logging.DEBUG)
timed_rotating_logger.propagate = False

# Rotate daily, keep 7 backup files
# 'midnight' is a common interval, or 'H' for hourly, 'M' for minute, etc.
timed_handler = logging.handlers.TimedRotatingFileHandler(
    timed_rotating_log_file,
    when='midnight', # Rotate at midnight
    interval=1,      # Every 1 day
    backupCount=7    # Keep 7 days of backups
)
timed_handler.setFormatter(formatter)
timed_rotating_logger.addHandler(timed_handler)

print("\n--- Testing TimedRotatingFileHandler (check timed_rotating_app.log) ---")
# For demonstration, we'll just log a few messages.
# Actual rotation happens based on system time, so you won't see new files immediately
# unless you run this code across midnight or change 'when' to 'S' for seconds (not recommended for production).
timed_rotating_logger.info("This message goes to the timed rotating log.")
timed_rotating_logger.debug("Another message for timed rotating log.")

# --- 8. Custom Log Levels ---
# While not common, you can define your own log levels.

# Define a new level (e.g., AUDIT)
AUDIT_LEVEL_NUM = 25 # Between INFO (20) and WARNING (30)
logging.addLevelName(AUDIT_LEVEL_NUM, "AUDIT")

def audit(self, message, *args, **kws):
    if self.isEnabledFor(AUDIT_LEVEL_NUM):
        self._log(AUDIT_LEVEL_NUM, message, args, **kws)

logging.Logger.audit = audit # Add the custom method to the Logger class

custom_level_logger = logging.getLogger("custom_level_logger")
custom_level_logger.setLevel(AUDIT_LEVEL_NUM)
custom_level_logger.propagate = False

# Add a console handler for this logger
custom_level_handler = logging.StreamHandler()
custom_level_handler.setLevel(AUDIT_LEVEL_NUM)
custom_level_handler.setFormatter(formatter)
custom_level_logger.addHandler(custom_level_handler)

print("\n--- Testing Custom Log Level (AUDIT) ---")
custom_level_logger.audit("This is an AUDIT message.")
custom_level_logger.info("This info message will also show because AUDIT_LEVEL_NUM is higher than INFO.")
custom_level_logger.debug("This debug message will NOT show as level is AUDIT.")

# --- 9. Filters ---
# Filters provide a more granular way to control which log records get processed by a handler.

class ContextFilter(logging.Filter):
    def filter(self, record):
        # Only allow messages if they contain 'important' in the message
        return 'important' in record.getMessage().lower()

filter_logger = logging.getLogger("filter_logger")
filter_logger.setLevel(logging.INFO)
filter_logger.propagate = False

filter_handler = logging.StreamHandler()
filter_handler.setFormatter(formatter)
filter_handler.addFilter(ContextFilter()) # Add the custom filter
filter_logger.addHandler(filter_handler)

print("\n--- Testing Custom Filter ---")
filter_logger.info("This message is not important and will be filtered out.")
filter_logger.info("This is an important message and should be logged.")
filter_logger.warning("Another important warning message.")

# --- 10. LoggerAdapter ---
# Used to inject contextual information into log messages.

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        # Add a 'user_id' field to the extra dictionary
        # This will be available in the formatter if you use %(user_id)s
        if 'extra' not in kwargs:
            kwargs["extra"] = {}
        kwargs["extra"]["user_id"] = self.extra.get("user_id", "N/A")
        return msg, kwargs

adapter_logger = logging.getLogger("adapter_logger")
adapter_logger.setLevel(logging.INFO)
adapter_logger.propagate = False

adapter_handler = logging.StreamHandler()
# New formatter to include 'user_id'
adapter_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - User:%(user_id)s - %(message)s')
adapter_handler.setFormatter(adapter_formatter)
adapter_logger.addHandler(adapter_handler)

# Create an adapter instance with initial context
user_specific_logger = CustomAdapter(adapter_logger, {'user_id': 'user_123'})

print("\n--- Testing LoggerAdapter ---")
user_specific_logger.info("User activity logged.")
user_specific_logger.warning("User encountered a minor issue.")

# You can change context dynamically
another_user_logger = CustomAdapter(adapter_logger, {'user_id': 'user_456'})
another_user_logger.error("Another user had a critical error.")

# --- 11. Capturing Warnings ---
# Direct warnings issued by the `warnings` module to the logging system.

print("\n--- Testing Capturing Warnings ---")
logging.captureWarnings(True) # Direct warnings to the logging system

# Issue a warning using the warnings module
warnings.warn("This is a warning from the warnings module!", UserWarning)
warnings.warn("Another warning that should appear in logs.", DeprecationWarning)

# Reset captureWarnings to default (False) if needed
# logging.captureWarnings(False)


print(f"\nCheck '{log_file_name}', '{dual_log_file_name}', '{rotating_log_file}' (and its backups), and '{timed_rotating_log_file}' for file output.")
